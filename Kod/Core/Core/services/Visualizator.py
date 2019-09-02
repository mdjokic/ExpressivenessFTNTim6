from abc import ABC, abstractmethod


class Visualizator(ABC):

    @abstractmethod
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
