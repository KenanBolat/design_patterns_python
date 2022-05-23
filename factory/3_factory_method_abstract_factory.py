from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is deliciouse')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is deliucouse')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water',
              f' pour {amount} ml, enjoy')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind Some beans, boil water',
              f' pour {amount} m, enjoy')
        return Coffee()


class HotDrinkMachninne:
    class AvailableDrinks(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self, ):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrinks:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks: ')
        for f in self.factories:
            print(f[0])

        s = input(f'please pick drink (0 - {len(self.factories)-1}):  ')
        idx = int(s)
        s = input(f'Specify Amount (ml) : ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)




def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


if __name__ == '__main__':
    # entry = input('What kind of drink would you like')
    # drink = make_drink(entry)
    hdm = HotDrinkMachninne()
    hdm.make_drink()
