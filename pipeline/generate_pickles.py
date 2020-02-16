#Libraries
import yaml
import logging.config
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

#Local Imports
from utils.parser import parse_text
from pipeline.input_pipeline import InputPipeline
from utils.metrics import get_metrics
from exceptions.exception import DatabaseNotFound
from settings import dictConfig

logging.config.dictConfig(dictConfig)
error_logger = logging.getLogger('error_logger')
debug_logger = logging.getLogger('debug_logger')




config = yaml.load(open('config.yml'))

try:
    input_pipe = InputPipeline()
    text_df = input_pipe.get_data_in_df(config["db"]["type"], config["db"]["db_name"], config["db"]["table_name"])
except DatabaseNotFound:
    error_logger.error("Unknown source. Change config")
    raise

list_corpus = text_df["TEXT"]
list_labels = text_df["CLASS_ID"]

X_train, X_test, y_train, y_test = train_test_split(list_corpus, list_labels, test_size=0.2, random_state=40)


count_vectorizer = CountVectorizer(analyzer='word', token_pattern=r'\w+')
bow = dict()
bow["train"] = (count_vectorizer.fit_transform(X_train), y_train)
bow["test"]  = (parse_text(X_test, count_vectorizer), y_test)
lr_classifier = LogisticRegression(C=30.0, class_weight='balanced', solver='newton-cg',
                         multi_class='multinomial', random_state=40)
embedding = bow
classifier = lr_classifier

classifier.fit(*embedding["train"])
y_predict = classifier.predict(embedding["test"][0])

joblib.dump(classifier, config["resource_dir"] + config["pickle"]["classifier_model_file"])
joblib.dump(count_vectorizer, config["resource_dir"] + config["pickle"]["preprocess_model_file"])


accuracy, precision, recall, f1 = get_metrics(embedding["test"][1], y_predict)
debug_logger.debug("accuracy = %.3f, precision = %.3f, recall = %.3f, f1 = %.3f" % (accuracy, precision, recall, f1))

