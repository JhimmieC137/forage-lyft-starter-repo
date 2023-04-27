from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, wear_arr:list):
        self.wear_arr = wear_arr
        
    @abstractmethod
    def needs_service(self):
        pass
    