from abc import ABC, abstractmethod

class Value(ABC):
    def __init__(self, initial_value, metric):
        self.value = initial_value 
        self.metric = metric

    @abstractmethod
    def increment(self):
        pass
    
