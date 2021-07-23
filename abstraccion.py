
class Washer:

    def __init__(self):
        pass

    def wash(self,temperature ='hot'):
        self._filling_the_water_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _filling_the_water_tank(self,temperature):
        print(f'Llenando el tanque con ague {temperature}')

    def _add_soap(self):
        print('Añadiendo jabon')

    def _wash(self):
        print('Lavando la ropa')

    def _centrifuge(self):
        print('Centrifugando la ropa')


if __name__ == '__main__':
    washer = Washer()
    washer.wash()