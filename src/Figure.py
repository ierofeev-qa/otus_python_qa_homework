class Figure:
    area = None

    def __init__(self):
        if isinstance(self, Figure):
            raise TypeError('Instantiation of the class Figure is forbidden')

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('An object of the unsupported class has been passed into the method')
        return self.area + figure.area
