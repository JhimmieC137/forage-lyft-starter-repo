import unittest
from datetime import datetime


from src.engines.capulet_engine import CapuletEngine
from src.engines.sternman_engine import SternmanEngine
from src.engines.willoughby_engine import WilloughbyEngine
from src.batteries.nubbin_battery import NubbinBattery
from src.batteries.spindler_battery import SpindlerBattery


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_not_be_service(self):
        current_mileage = 0
        last_service_mileage = 30000
        
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
        
    def test_battery_should_be_serviced(self):
        current_mileage = 70001
        last_service_mileage = 40000
        
        car = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_not_be_service(self):
        current_mileage = 0
        last_service_mileage = 60000
        
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
        
    def test_battery_should_be_serviced(self):
        current_mileage = 70001
        last_service_mileage = 10000
        
        car = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_not_be_service(self):
        warning_light_on = False
        
        car = SternmanEngine(warning_light_on)
        self.assertFalse(car.needs_service())
        
    def test_battery_should_be_serviced(self):
        warning_light_on = True
        
        car = SternmanEngine(warning_light_on)
        self.assertTrue(car.needs_service())
        
        
        


class TestNubbinBattery(unittest.TestCase):
    def test_engine_should_not_be_service(self):
        current_date = datetime.today().date()  
        last_service_date = datetime.today().date().replace(year=current_date.year - 4)
        
        car = NubbinBattery(current_date, last_service_date)
        self.assertFalse(car.needs_service())
        
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()  
        last_service_date = datetime.today().date().replace(year=current_date.year - 7)
        
        car = NubbinBattery(current_date, last_service_date)
        self.assertTrue(car.needs_service())
        
        


class TestSpindlerBattery(unittest.TestCase):
    def test_engine_should_not_be_service(self):
        current_date = datetime.today().date()  
        last_service_date = datetime.today().date().replace(year=current_date.year - 2)
        
        car = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(car.needs_service())
        
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()  
        last_service_date = datetime.today().date().replace(year=current_date.year - 7)
        
        car = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(car.needs_service())
        


if __name__ == '__main__':
    unittest.main()
