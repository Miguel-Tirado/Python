from car import Car
# from the car module import the Car class 

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer = 23
my_new_car.read_odometer()