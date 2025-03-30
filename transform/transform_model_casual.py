import pickle
from sklearn.ensemble import RandomForestRegressor
from transform.transform_model_base import TransformModelBase

class TransformModelCasual(TransformModelBase):

    def __init__(self, config):
        self.config = config
        self._load_dependency(self.config.MODEL_CASUAL_PATH)

    def predict(self, dataset):
        results = self.model.predict(dataset)
        return results
