import re
import yaml

import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report
from sklearn.externals import joblib


from utils.db_sqlite import get_db_connector
from pipeline.preprocessing import parse_text


def standardize_text(df, text_field):
    # normalize by turning all letters into lowercase
    df[text_field] = df[text_field].str.lower()
    # get rid of URLS
    df[text_field] = df[text_field].apply(lambda elem: re.sub(r"http\S+", "", elem))
    return df


def get_metrics(y_test, y_predicted):
    # true positives / (true positives+false positives)
    precision = precision_score(y_test, y_predicted, pos_label=None,
                                average='weighted')
    # true positives / (true positives + false negatives)
    recall = recall_score(y_test, y_predicted, pos_label=None,
                          average='weighted')

    # harmonic mean of precision and recall
    f1 = f1_score(y_test, y_predicted, pos_label=None, average='weighted')

    # true positives + true negatives/ total
    accuracy = accuracy_score(y_test, y_predicted)
    return accuracy, precision, recall, f1

conn = get_db_connector()
config = yaml.load(open('config.yml'))

text_df = pd.read_sql_query("SELECT * FROM data", conn)
text_df = standardize_text(text_df, "TEXT")
#tokenizer = RegexpTokenizer(r'\w+')

#text_df["TOKENS"] = text_df["TEXT"].apply(tokenizer.tokenize)


list_corpus = text_df["TEXT"]
list_labels = text_df["CLASS_ID"]

X_train, X_test, y_train, y_test = train_test_split(list_corpus, list_labels, test_size=0.2, random_state=40)

count_vectorizer = CountVectorizer(analyzer='word', token_pattern=r'\w+')
bow = dict()
bow["train"] = (count_vectorizer.fit_transform(X_train), y_train)
joblib.dump(count_vectorizer, config["resource_dir"] + config["pickle"]["preprocess_model_file"])
bow["test"]  = (parse_text(X_test, count_vectorizer), y_test)


lr_classifier = LogisticRegression(C=30.0, class_weight='balanced', solver='newton-cg',
                         multi_class='multinomial', random_state=40)

embedding = bow
classifier = lr_classifier

classifier.fit(*embedding["train"])
#import ipdb; ipdb.set_trace()
y_predict = classifier.predict(embedding["test"][0])
joblib.dump(classifier, config["resource_dir"] + config["pickle"]["classifier_model_file"])


#import ipdb; ipdb.set_trace()
accuracy, precision, recall, f1 = get_metrics(embedding["test"][1], y_predict)
print("accuracy = %.3f, precision = %.3f, recall = %.3f, f1 = %.3f" % (accuracy, precision, recall, f1))

#import ipdb; ipdb.set_trace()

"""
import ipdb; ipdb.set_trace()
lr_classifier = LogisticRegression(C=30.0, class_weight='balanced', solver='newton-cg',
                         multi_class='multinomial', random_state=40)

lr_classifier.fit(X_train, y_train)


import ipdb; ipdb.set_trace()
"""

