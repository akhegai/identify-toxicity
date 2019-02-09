import numpy as np
import pandas as pd
import scipy.sparse as sparse
from .constants import TARGET_LABELS
from .train_model import train_model, get_tokenizer
from .model_manager import save_model, load_model, save_bow, load_bow

def create_and_save_model(data_path, output_model_path, output_tokenizer_path):
    data = pd.read_csv(data_path)
    model, tokenizer = train_model(data)
    save_model(model, output_model_path)
    save_bow(tokenizer, output_tokenizer_path)


def get_trained_model(path):
    return load_model(path)

def get_trained_bow(path):
    return load_bow(path)

class Classifier:

    def __init__(self, estimator_path, bow_path):
        self.estimator = get_trained_model(estimator_path)
        self.bow = get_trained_bow(bow_path)

    def serialize_prediction(self, prediction):
        serialized_prediction = {}
        for i in range(len(prediction)):
            serialized_prediction[TARGET_LABELS[i]] = bool(prediction[i])
        return serialized_prediction
            
    def serialize(self, predictions):
        return [self.serialize_prediction(prediction) for prediction in predictions]

    def predict(self, data):
        transformed_data = self.bow.transform(pd.Series(data))
        predictions = self.estimator.predict(transformed_data)
        return self.serialize(predictions)
