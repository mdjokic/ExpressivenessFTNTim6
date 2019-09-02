from abc import ABC, abstractmethod


class DataMaker(ABC):

    @abstractmethod
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    @abstractmethod
    def create_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def send_data(self, payload):
        pass
