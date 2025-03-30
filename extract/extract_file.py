from extract.extract_base import ExtractBase
import pandas as pd

class ExtractFile(ExtractBase):

    def __init__(self, config):
        self.config = config

    def load_data(self, config):
        return pd.read_csv(config.DATA_PATH)
