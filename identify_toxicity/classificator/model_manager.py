import pickle


def save_model(model, path):
    with open(path, 'wb') as sfile:
        pickle.dump(model, sfile)


def load_model(path):
    with open(path, 'rb') as lfile:
        return pickle.load(lfile)


def save_bow(bow, path):
    with open(path, 'wb') as sfile:
        pickle.dump(bow, sfile)


def load_bow(path):
    with open(path, 'rb') as lfile:
        return pickle.load(lfile)
