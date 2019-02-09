import os

from identify_toxicity.constants.paths import TRAIN_DATA_PATH,TRAINED_NBSVM_PATH, TFIDF_BOW_PATH
from identify_toxicity.classificator.model import create_and_save_model

create_and_save_model(TRAIN_DATA_PATH, TRAINED_NBSVM_PATH, TFIDF_BOW_PATH)
