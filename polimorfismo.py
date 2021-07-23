

class Person:

    def __init__(self, name):
        self.name = name

    def advance(self):
        print('Ando caminando')


class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def advance(self):
        print('Ando moviendome en mi bicicleta')


if __name__ == "__main__":
    person = Person('Daniel')
    print(person.advance())

    cyclist = Cyclist('Daniel')
    print(cyclist.advance())