import pickle

from sklearn.ensemble import RandomForestRegressor

from transform.transform_model_base import TransformModelBase


class TransformModelRegistered(TransformModelBase):

    def __init__(self, config):
        self.config = config
        self._load_dependency(self.config.MODEL_REGISTERED_PATH)

    def predict(self, dataset):
        results = self.model.predict(dataset)
        return results
