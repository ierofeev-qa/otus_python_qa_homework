import math
from src.Figure import Figure


class Circle(Figure):
    name = "Circle"

    def __init__(self, radius):
        super(Figure, self).__init__()
        self.__radius = radius

    @property
    def area(self):
        return math.pi * (self.__radius ** 2)

    @property
    def perimeter(self):
        return math.pi * self.__radius * 2
