class Person:
    def __init__(self):
        self.name = None
        self.positon = None
        self.DOB = None

    def __str__(self):
        return f'{self.name} born on {self.DOB} ' + \
               f'works as  {self.positon}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder():
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.positon = position
        return self


class PersonDOBBuilder(PersonJobBuilder):
    def born(self, DOB):
        self.person.DOB = DOB
        return self

pb = PersonDOBBuilder()
me = pb.called('Dimitri').works_as_a('Quant').born('1982').build()
print(me)