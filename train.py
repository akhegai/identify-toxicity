import os

from identify_toxicity.classificator.model import create_and_save_model

DEFAULT_MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/models/'
DEFAULT_DATA_PATH = os.path.dirname(os.path.realpath(__file__)) + '/data/train.csv'

create_and_save_model(DEFAULT_DATA_PATH, DEFAULT_MODEL_PATH)
