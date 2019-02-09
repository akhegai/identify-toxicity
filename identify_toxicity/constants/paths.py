import os
from pathlib import Path

TRAINED_NBSVM_FILENAME = 'trained_nbsvm_classifier_x64.cav'
TFIDF_MATRIX_FILENAME = 'tfidf_bow_x64.cav'
TRAIN_DATA_PATH = 'train.csv'

ROOT_DIR = Path(
    os.path.dirname(
        os.path.abspath(__file__))).parent.parent

DATA_DIR_PATH = os.path.join(ROOT_DIR, "data")
MODELS_DIR_PATH = os.path.join(ROOT_DIR, "models")

TRAIN_DATA_PATH = os.path.join(DATA_DIR_PATH, TRAIN_DATA_PATH)
TRAINED_NBSVM_PATH = os.path.join(MODELS_DIR_PATH, TRAINED_NBSVM_FILENAME)
TFIDF_MATRIX_PATH = os.path.join(MODELS_DIR_PATH, TFIDF_MATRIX_FILENAME)