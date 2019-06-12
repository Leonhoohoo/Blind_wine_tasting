
import numpy as np
import pandas as pd
from config import *

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.metrics import confusion_matrix
from sklearn.manifold import MDS


# ---------------------------- Basic ----------------------------


def display_all(df):
    with pd.option_context("display.max_rows", 1000):
        with pd.option_context("display.max_columns", 1000):
            display(df)
            

# ------------------------ Preprocessing ------------------------

# drop the row of variety <= drop_condition
def drop(name_columns, drop_condition, data_old, data_new):
    '''drop form name_columns by drop_condition'''
    data_new = data_old
    for i in drop_condition:
        data_old = data_new
        x = data_old[name_columns] != i
        data_new = data_old[x]
    return data_new


# Split arrays or matrices into proportion train and test subsets 
def spilt_vals(data, proportion, **random_state):
    test = pd.DataFrame()
    proportion = 1 - proportion
    for i in data.variety.factorize()[1]:
        x = data['variety'] == i
        valid = data[x]
        valid = valid.sample(frac=proportion, **random_state)
        test = test.append(valid)
    data = data.drop(test.index)
    data = data.reset_index(drop=True)
    test = test.reset_index(drop=True)
    return data, test


# -------------------- Featurne Engineering ---------------------


def mds_count(train_texts, test_texts,n):
    df_texts = pd.concat([train_texts, test_texts])
    kwargs = {
            'strip_accents': 'unicode',
            'decode_error': 'replace',
            'analyzer': TOKEN_MODE,  # Split text into word tokens.
            'min_df': MIN_DOCUMENT_FREQUENCY,
    }
    vectorizer = CountVectorizer(**kwargs)
    df_texts = vectorizer.fit_transform(df_texts)
    df_texts = pd.DataFrame(df_texts.todense())
    corr = df_texts.T.corr()
    distance = corr.applymap(lambda x: 1-x**2)
    embedding = MDS(n_jobs=-1,n_components=n, dissimilarity='precomputed', random_state=RANDOM_SEED)
    mds = embedding.fit_transform(distance)
    train = mds[:len(train_texts), :]
    test = mds[len(train_texts)::, :]
    return train, test



def ngram_vectorize(train_texts, train_labels, test_texts):
    """Vectorizes texts as n-gram vectors.

    1 text = 1 tf-idf vector the length of vocabulary of unigrams + bigrams.

    # Arguments
        train_texts: list, training text strings.
        train_labels: np.ndarray, training labels.
        val_texts: list, validation text strings.

    # Returns
        x_train, x_val: vectorized training and validation texts
    """
    # Create keyword arguments to pass to the 'tf-idf' vectorizer.
    kwargs = {
            'ngram_range': NGRAM_RANGE,  # Use 1-grams + 2-grams.
            'strip_accents': 'unicode',
            'decode_error': 'replace',
            'analyzer': TOKEN_MODE,  # Split text into word tokens.
            'min_df': MIN_DOCUMENT_FREQUENCY,
    }
    vectorizer = TfidfVectorizer(**kwargs)

    # Learn vocabulary from training texts and vectorize training texts.
    x_train = vectorizer.fit_transform(train_texts)

    # Vectorize validation texts.
    x_test = vectorizer.transform(test_texts)

    # Select top 'k' of the vectorized features.
    selector = SelectKBest(f_classif, k=min(TOP_K, x_train.shape[1]))
    selector.fit(x_train, train_labels)
    x_train = selector.transform(x_train).astype('float32')
    x_test = selector.transform(x_test).astype('float32')
    return x_train, x_test


#Confusion matrix
def con_matrix(df, y_test, pred_test):
    variety = df.variety.value_counts().index
    labels_variety = []
    for i in variety:
        data = df[df.variety == i]
        data = data.reset_index()
        labels_variety.append(data.labels_variety[0])
    confusion = confusion_matrix(y_test, pred_test, labels=labels_variety)
    index = pd.Index(variety, name="Real")
    confusion = pd.DataFrame(confusion, index=index, columns=variety)
    return confusion

def con_matrix_two(df, y_test, pred_test):
    labels = ['Red', 'White']
    confusion = confusion_matrix(y_test, pred_test)
    index = pd.Index(labels, name="Real")
    confusion = pd.DataFrame(confusion, index=index, columns=labels)
    return confusion




#-------------------- Ensemble Selection -----------------------

