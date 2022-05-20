# open closed principle (ocp)
""" open for extension, closed for modification"""
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.Size = size

# this class vioaletes ocp


class ProductFilter:

    def filter_by_color(self, product, color):
        for p in product:
            if p.color == color: yield p

    def filter_by_size(self, product, size):
        for p in product:
            if p.size == size: yield p

    def filter_by_size_color(self, product, color, size):
        for p in product:
            if p.color == color and p.size == size: yield p


class Specification:
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):

    def __init__(self, size):
        self.Size = size

    def is_satisfied(self, item):
        return item.Size == self.Size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', color=Color.BLUE, size=Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green Products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    better = BetterFilter()
    large = SizeSpecification(Size.LARGE)
    for p in better.filter(products, large):
        print(f' - {p.name} is large')

    large_blue = large and ColorSpecification(Color.BLUE)

    for p in better.filter(products, large_blue):
        print(f' - {p.name} is large and  blue')

