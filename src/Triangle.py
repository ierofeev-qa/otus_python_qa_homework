import math
from src.Figure import Figure


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, side_one, side_two, side_three):
        super(Figure).__init__()
        self.__side_one = side_one
        self.__side_two = side_two
        self.__side_three = side_three

    @staticmethod
    def triangle_is_exist(side_one, side_two, side_three):
        return side_one + side_two > side_three and side_one + side_three > side_two and side_two + side_three > side_one

    def __new__(cls, side_one, side_two, side_three):
        if cls.triangle_is_exist(side_one, side_two, side_three):
            instance = super(Triangle, cls).__new__(cls)
            instance.side_one, instance.side_two, instance.side_three = side_one, side_two, side_three
            return instance
        return None

    @property
    def area(self):
        semi_per = (self.__side_one + self.__side_two + self.__side_three) / 2
        return math.sqrt(
            semi_per * (semi_per - self.__side_one) * (semi_per - self.__side_two) * (semi_per - self.__side_three)
        )

    @property
    def perimeter(self):
        return self.__side_one + self.__side_two + self.__side_three
