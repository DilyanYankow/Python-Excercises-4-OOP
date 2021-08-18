# class Rectangle:
#     pass
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width  = width
#
# class Cube(Rectangle):
#
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width  = width
#         self.height = height
# NO

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.length*self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square1 = Square(3, 3)
cube1 = Cube(3, 3, 3)

print(square1.area())
print(cube1.volume())