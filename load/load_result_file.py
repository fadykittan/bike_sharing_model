import os
import numpy as np
from load.load_result_base import LoadResultBase


class LoadResultFile(LoadResultBase):

    def __init__(self, config):
        self.path = config.OUTPUT_PATH

    def save(self, result, file_name):
        os.makedirs(self.path, exist_ok=True)
        np.savetxt(self.path + file_name, result, delimiter=',')
