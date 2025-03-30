import abc
import pickle

from sklearn.ensemble import RandomForestRegressor


class TransformModelBase(abc.ABC):

    def _load_dependency(self, path):
        with open(path, 'rb') as f:
            self.model: RandomForestRegressor = pickle.load(f)

    @abc.abstractmethod
    def predict(self, dataset):
        pass


