from abc import ABC, abstractmethod

class LoadResultBase(ABC):

    @abstractmethod
    def save(self, result, file_name):
        pass
