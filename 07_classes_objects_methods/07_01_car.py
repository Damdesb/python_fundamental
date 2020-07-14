'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"your car is a {self.model}, from {self.year}, Its max speed is {self.max_speed}"

    def use(self, speed_change):
        self.max_speed += speed_change


car_1 = car('Peugeot', 2005, 160)
# car_2 = car('Holden', 2020, 145)
# car_3 = car('Ferrari', 2020, 260)

car_1.use(5)
print(car_1)
# print(car_2)
# print(car_3)
