import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address} , {self.city} , {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} live at {self.address}'


address = Address('123 London Road', 'London', 'UK')
john = Person('John', address)

# copies ignoring references and copy the values
jane = copy.deepcopy(john)

jane.name = 'Jane'
jane.address.street_address = '123b London Road'

print(john)
print(jane)
