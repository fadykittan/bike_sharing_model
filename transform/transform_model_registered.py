import pickle

from sklearn.ensemble import RandomForestRegressor

from transform.transform_model_base import TransformModelBase


class TransformModelRegistered(TransformModelBase):

    def __init__(self, config):
        self.model = None
        self.config = config

    def __load_dependency(self):
        with open(self.config.MODEL_REGISTERED_PATH, 'rb') as f:
            self.model: RandomForestRegressor = pickle.load(f)

    def predict(self, dataset):
        self.__load_dependency()
        results = self.model.predict(dataset)
        return results