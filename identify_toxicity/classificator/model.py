import numpy as np
import pandas as pd
import scipy.sparse as sparse
from .train_model import train_model
from .model_manager import save_model, load_model


class Classifier:

    def __init__(self, estimator, bow):
        self.estimator = estimator
        self.bow = bow

    def classify(self, data):
        sparse()
        return self.estimator.predict()


def create_and_save_model(data_path, output_path):
    data = pd.read_csv(data_path)
    model = train_model(data)
    save_model(model, output_path)


def get_trained_model(path):
    return load_model(path)
