from abc import ABC
from csv import csv
from pprint import pprint

# class Cupcake:
#     def __init__(self, name, price, flavor, frosting, filling):
#         self.name = name
#         self.price = price
#         self.flavor = flavor
#         self.frosting = frosting
#         self.filling = filling
#         self.sprinkles = []

#     def add_sprinkles(self, *args):
#         for sprinkle in args:
#             self.sprinkles.append(sprinkle)


# my_cupcake = Cupcake('Cookies and Cream', 2.99, 'Chocolate', 'Oreo', 'Vanilla', True)
# print(my_cupcake)

# my_cupcake.add_sprinkles('Oreo crumbs', 'Chocolate', 'Vanilla')
# print(my_cupcake.sprinkles)

# my_cupcake.frosting = 'Chocolate'
# my_cupcake.filling = 'Chocolate'
# my_cupcake.name = 'Triple Chocolate'
# print(my_cupcake)

# my_cupcake.is_miniature = False
# print(my_cupcake.is_miniature)


class Cupcake:
    size = 'regular'
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = 'mini'

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self. sprinkles = []

my_cupcake_mini = Mini('Chocolate', 1.99, 'Chocolate', 'White')

print(my_cupcake_mini.name)

class Cupcake(ABC):
    size = 'regular'

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

read_csv('sample.csv')

cupcake1 = Regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3
]

def write_new_csv(file, cupcakes):
    with open(file, 'w', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattribute(cupcake, 'filling'):
                writer.writerow({'size': cupcake.size, 'name': cupcake.name, 'price': cupcake.price, 'flavor': cupcake.flavor, 'frosting': cupcake.frosting, 'filling': cupcake.filling, 'sprinkles': cupcake.sprinkles})
            else:
                writer.writerow({'size': cupcake.size, 'name': cupcake.name, 'price': cupcake.price, 'flavor': cupcake.flavor, 'frosting': cupcake.frosting, 'sprinkles': cupcake.sprinkles})

def add_cupcake(file, cupcake):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattribute(cupcake, 'filling'):
                writer.writerow({'size': cupcake.size, 'name': cupcake.name, 'price': cupcake.price, 'flavor': cupcake.flavor, 'frosting': cupcake.frosting, 'filling': cupcake.filling, 'sprinkles': cupcake.sprinkles})
            else:
                writer.writerow({'size': cupcake.size, 'name': cupcake.name, 'price': cupcake.price, 'flavor': cupcake.flavor, 'frosting': cupcake.frosting, 'sprinkles': cupcake.sprinkles})