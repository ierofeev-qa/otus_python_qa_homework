import pytest

from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


@pytest.fixture
def default_triangle():
    triangle = Triangle(side_a=4, side_b=4, side_c=4)
    yield triangle
    del triangle


@pytest.fixture
def nonexistent_triangle():
    triangle = Triangle(side_a=5, side_b=20, side_c=100)
    yield triangle
    del triangle


@pytest.fixture
def default_square():
    square = Square(side=6)
    yield square
    del square


@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(side_one=3, side_two=4)
    yield rectangle
    del rectangle


@pytest.fixture
def default_circle():
    circle = Circle(radius=7)
    yield circle
    del circle
