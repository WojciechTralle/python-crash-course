# Aliases
from car_v2 import Car
from electric_car_v2 import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())