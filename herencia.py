
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Cube(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)



if __name__ == '__main__':
    rectangle = Rectangle(4,6)
    print(rectangle.area())

    cube = Cube(8)
    print(cube.area())