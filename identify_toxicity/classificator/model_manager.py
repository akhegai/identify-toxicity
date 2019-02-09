import pickle

MODEL_FILENAME = 'trained_nbsvm_classifier_x64.cav'
MODEL_BOW = 'nbsvm_bow.cav'


def save_model(model, path):
    with open(path + '/' + MODEL_FILENAME, 'wb') as sfile:
        pickle.dump(model, sfile)


def load_model(path):
    with open(path, 'rb') as lfile:
        return pickle.load(lfile)


def save_bow(bow, path):
    with open(path + '/' + MODEL_FILENAME, 'wb') as sfile:
        pickle.dump(bow, sfile)


def load_bow(path):
    with open(path + '/' + MODEL_BOW, 'rb') as lfile:
        return pickle.load(lfile)
