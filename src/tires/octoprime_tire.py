from ..tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear_arr:list):
        self.wear_arr = wear_arr
        
    def needs_service(self):
        if sum(self.wear_arr) >= 3:
            return True
        else:
            return False