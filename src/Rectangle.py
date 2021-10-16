from src.Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, side_one, side_two):
        super(Figure).__init__()
        self.__side_one = side_one
        self.__side_two = side_two

    @property
    def area(self):
        return self.__side_one * self.__side_two

    @property
    def perimeter(self):
        return 2 * (self.__side_one + self.__side_two)
