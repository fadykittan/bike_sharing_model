from math import sin
from math import cos
from math import pi
import pandas as pd

class TransformProcessing():

    def __init__(self, config):
        self.config = config

    def transform(self, dataset):
        dataset = self.__transform_date(dataset)
        dataset = self.__convert_time(dataset)
        dataset = self.__drop_column(dataset)
        dataset = self.__get_columns_for_prediction(dataset)
        return dataset

    @staticmethod
    def __transform_date(dataset):
        dataset['year'] = pd.to_datetime(dataset.datetime).dt.year
        dataset['month'] = pd.to_datetime(dataset.datetime).dt.month
        dataset['hour'] = pd.to_datetime(dataset.datetime).dt.hour
        dataset['weekday'] = pd.to_datetime(dataset.datetime).dt.weekday
        return dataset

    @staticmethod
    def __convert_time(dataset):
        dataset['hour_x'] = dataset['hour'].apply(lambda x: sin(2 * pi * x / 24))
        dataset['hour_y'] = dataset['hour'].apply(lambda x: cos(2 * pi * x / 24))
        return dataset

    @staticmethod
    def __drop_column(dataset):
        drop_columns = ['atemp', 'season', 'holiday', 'weekday', 'hour']
        dataset.drop(drop_columns, axis=1, inplace=True)
        return dataset

    @staticmethod
    def __get_columns_for_prediction(dataset):
        predict_columns = ['year', 'month', 'hour_x', 'hour_y', 'temp', 'humidity', 'windspeed']
        dataset_to_predict = dataset[predict_columns]
        return dataset_to_predict