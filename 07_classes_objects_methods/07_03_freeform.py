'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


# create classes of alcohol family

class wine:
    revenue = 'beverage'
    family = 'alcohol family'

    def __init__(self, name, vintage, grape, region, luc):
        self.name = name
        self.vintage = vintage
        self.grape = grape
        self.region = region
        self.luc = luc

    def get_data(self):
        print(
            f'This wine is a {self.name}, from {self.vintage}, made with {self.grape}, from {self.region}, cost is ${self.luc}')

    def use(self, new_vintage, new_luc):
        self.vintage += new_vintage
        self.luc = new_luc
        print(f'The new vintage')

    def __str__(self):
        return f'new vintage for {self.name} is {self.vintage}'


wine_1 = wine('Petrus', 2019, 'cabernet', 'Bordeaux', 999)
wine_2 = wine('Margaux', 2002, 'merlot', 'Bordeaux', 1299)

# print(wine_1)
# wine_1.get_data()
# wine_2.get_data()
wine_2.use(0, 1200)
# wine_2.get_data()
