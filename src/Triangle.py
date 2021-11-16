import math
from src.Figure import Figure


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, side_a, side_b, side_c):
        super(Figure, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    @staticmethod
    def triangle_is_exist(side_a, side_b, side_c):
        return side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a

    def __new__(cls, side_a, side_b, side_c):
        if cls.triangle_is_exist(side_a, side_b, side_c):
            instance = super(Triangle, cls).__new__(cls)
            instance.side_a, instance.side_b, instance.side_c = side_a, side_b, side_c
            return instance
        return None

    @property
    def area(self):
        semi_per = (self.__side_a + self.__side_b + self.__side_c) / 2
        return math.sqrt(
            semi_per *
            (semi_per - self.__side_a) *
            (semi_per - self.__side_b) *
            (semi_per - self.__side_c)
        )

    @property
    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c
