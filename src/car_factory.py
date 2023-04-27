from datetime import date
from engines.capulet_engine import CapuletEngine
from engines.willoughby_engine import WilloughbyEngine
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery
from batteries.nubbin_battery import NubbinBattery


class CarFactory:
    def __init__(self):
        self.needs_service = 0
        
        
    def create_calliope(self, current_date:date, last_service_date: date, current_mileage: int, last_service_mileage: int, wear_arr:list):
        engine = CapuletEngine(current_mileage, last_service_mileage).needs_service()
        battery = SpindlerBattery(current_date, last_service_date).needs_service()
        if engine or battery:
            self.needs_service = True
        else:
            self.needs_service = False
    
    
    def create_glissade(self, current_date:date, last_service_date: date, current_mileage: int, last_service_mileage: int, wear_arr:list):
        engine = WilloughbyEngine(current_mileage, last_service_mileage).needs_service()
        battery = SpindlerBattery(current_date, last_service_date).needs_service()
        if engine or battery:
            self.needs_service = True
        else:
            self.needs_service = False
    
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on, wear_arr:list):
        engine = SternmanEngine(warning_light_on).needs_service()
        battery = SpindlerBattery(current_date, last_service_date).needs_service()
        if engine or battery:
            self.needs_service = True
        else:
            self.needs_service = False
    
    
    def create_rorschach(self, current_date:date, last_service_date: date, current_mileage: int, last_service_mileage: int, wear_arr:list):
        engine = WilloughbyEngine(current_mileage, last_service_mileage).needs_service()
        battery = NubbinBattery(current_date, last_service_date).needs_service()
        if engine or battery:
            self.needs_service = True
        else:
            self.needs_service = False
    
    
    def create_thovex(self, current_date:date, last_service_date: date, current_mileage: int, last_service_mileage: int, wear_arr:list):
        engine = CapuletEngine(current_mileage, last_service_mileage).needs_service()
        battery = NubbinBattery(current_date, last_service_date).needs_service()
        if engine or battery:
            self.needs_service = True
        else:
            self.needs_service = False