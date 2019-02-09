import sklearn.feature_extraction.text as fe_text
from sklearn.multiclass import OneVsRestClassifier
from .df_utils import *
from .lib.nb_svm_classifier import NbSvmClassifier


def get_tokenizer():
    return fe_text.TfidfVectorizer(ngram_range=(1, 2),
                                   min_df=3, max_df=0.9, strip_accents='unicode', use_idf=1,
                                   smooth_idf=1, sublinear_tf=1)


def train_model(data):
    x, y = get_data_and_targets(data)
    x_trainsformed = get_tokenizer().fit_transform(x)
    classifier = OneVsRestClassifier(NbSvmClassifier(C=4, dual=True, n_jobs=-1))
    classifier.fit(x_trainsformed, y)
    return classifier
