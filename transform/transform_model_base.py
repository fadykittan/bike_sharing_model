import abc
import pickle

from sklearn.ensemble import RandomForestRegressor


class TransformModelBase(abc.ABC):

    @abc.abstractmethod
    def predict(self, dataset):
        pass


