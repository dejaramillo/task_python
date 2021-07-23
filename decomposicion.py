
class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'idle'
        self._motor = Motor(cylinders = 4)

    def acelerate(self, type='slowly'):
        if type == 'fast':
            self._motor.fuel_injection(10)
        else:
            self._motor.fuel_injection(3)

        self._state = 'on_the_move'

class Motor:

    def __init__(self, cylinders, type= 'fuel'):
        self.cylinders = cylinders
        self.type = type
        self.temperature = 0

    def fuel_injection(self, quantity):
        pass
