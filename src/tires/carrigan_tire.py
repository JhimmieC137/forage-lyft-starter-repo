from ..tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_arr:list):
        self.wear_arr = wear_arr
        
    def needs_service(self):
        for numbers in self.wear_arr:
            if numbers >= 0.9: 
                return True
        return False