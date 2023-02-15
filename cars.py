# Classes can be written with or without parens
class Car:
    # Class attributes
    wheels = 4
    doors = 2
    engine = True

    # Instance attributes are created with initializer inside the class
    # Put defaults at the end of init method
    def __init__(self, model, year, make="Ford"):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        # Instance attributes do not always have to be passed in
        self.is_moving = False

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    # Other is what you are comparing class instance to

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model

    # Function inside class is a "method"
    # All methods inside a class must take self as an arguement or will throw an error

    def stop(self):
        if self.is_moving:
            print('The car has stopped')
            self.is_moving = False
        else:
            print('The car has already stopped')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('The car starts moving')
                self.is_moving = True
            print(f'The car is going {speed}')
        else:
            print('You have run out of gas')
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True


class Dealership:
    def __init__(self):
        # self.cars = ["Ford Fusion", "Honda Civic", "Dodge Dakota"]
        self.cars = []

    def __iter__(self):
        # yield from tells python to grab ever iterable from the list and return it
        yield from self.cars

    def add_car(self, car):
        self.cars.append(car)

# my_car = Car()

# print(my_car)  # <__main__.Car object at 0x104373370>
# print(type(my_car))  # <class '__main__.Car'>
# print(isinstance(my_car, Car)) # True


# If you try and constuct an object without init attributes you get --> Car.__init__() missing 3 required positional arguments: 'make', 'model', and 'year' (do not need self)
car_one = Car("Model T", 1908)
# car_two = Car("Phantom", 2020, "Rolls Royce")
# print(car_one.doors) # 2
# print(car_two.doors) # 2
# # Class attributes can be accessed without creating an instance
# print(Car.doors) # 2
# # Change attributes on instance of class
# car_one.doors = 4
# print(car_one.doors) # 4
# If you change the attribute on the class it changes it for all instances
# Car.doors = 4
# print(car_one.doors) # 4
# print(car_two.doors) # 4
# If you change both the class and the instance attributes the attribute change on the instance overrides class
# Car.doors = 6
# car_one.doors = 8
# print(car_one.doors) # 8

# Accessing attributes
# print(car_one.make) # Ford
# print(car_two.make) # Rolls Royce
# # Instance attributes can only be accessed with an instance
# print(Car.make)  # type object 'Car' has no attribute 'make'

# Changing attributes
# car_one.year = 2015
# print(car_one.year) # 2015

# Calling methods
# car_one.stop()  # The car has already stopped
# car_one.go('slow')  # The car starts moving \n The car is going slow
# car_one.go('fast')  # You have run out of gas \n The car has stopped

# Dunder methods
# print(dir(car_one))
# __str__
# Printing car gives the __str__ method
# print(car_one)  # Ford Model T 1908
# __iter__
my_dealership = Dealership()
for car in my_dealership:
    print(car)
    # Ford Fusion
    # Honda Civic
    # Dodge Dakota

# Adding classes together
car_two = Car("Fusion", 1990)
# car_three = Car("Fiesta", 2000)
# my_dealership.add_car(car_one)
# my_dealership.add_car(car_two)
# my_dealership.add_car(car_three)
# for car in my_dealership:
#     print(car)
    # Ford Model T 1908
    # Ford Fusion 1990
    # Ford Fiesta 2000

# Comparing class instances
# __eq__
# if car_one == car_two:
#     print('equal')
# else:
#     print('not equal')
# not equal
# Switch make and model to be equal
car_two = Car("Model T", 1990)
# if car_one == car_two:
#     print('equal')
# else:
#     print('not equal')
# equal
