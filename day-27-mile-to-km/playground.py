def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print("Addition of 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 is: ")
print(add(2, 3, 4, 5, 6, 7, 8, 9, 10))

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

print("2 + 3 * 5")
print(calculate(2,add=3,multiply=5))

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="Skyline")

print(my_car.model)