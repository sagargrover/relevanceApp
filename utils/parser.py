#Libraries
import re

#Local imports

def standardize_text(df, text_field):
    # normalize by turning all letters into lowercase
    df[text_field] = df[text_field].str.lower()
    # get rid of URLS
    df[text_field] = df[text_field].apply(lambda elem: re.sub(r"http\S+", "", elem))
    return df

def parse_text(data, count_vectorizer):
    return count_vectorizer.transform(data)