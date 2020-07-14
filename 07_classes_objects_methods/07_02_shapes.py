'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"the area from this rectangle is {self.length * self.width}. Its perimeter is " \
               f"{self.length + self.width}"


class circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"the area from this circle is {3.14 * self.radius ** 2}. It's circumference is " \
               f"{2 * 3.14 * self.radius}"


r = rectangle(3, 6)
print(r)
c = circle(5)
print(c)
