from src.Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, side):
        super(Figure, self).__init__()
        self.__side = side

    @property
    def area(self):
        return self.__side ** 2

    @property
    def perimeter(self):
        return self.__side * 4
