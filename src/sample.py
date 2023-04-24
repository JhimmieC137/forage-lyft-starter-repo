from datetime import datetime
from car_factory import CarFactory

today = datetime.today().date()
today = today.replace(year=today.year + 4)

car = CarFactory()
car.create_palindrome(today, datetime.today().date(), False)
print(car.needs_service)

