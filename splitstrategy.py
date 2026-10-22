from abc import ABC,abstractmethod

class SplitStrategy(ABC):

    @abstractmethod
    
    def split(self,amount:float, users:list):
        pass