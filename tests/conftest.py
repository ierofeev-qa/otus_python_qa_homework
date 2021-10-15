import pytest

from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


@pytest.fixture
def default_triangle():
    triangle = Triangle(4, 4, 4)
    yield triangle
    del triangle


@pytest.fixture
def nonexistent_triangle():
    triangle = Triangle(5, 20, 100)
    yield triangle
    del triangle


@pytest.fixture
def default_square():
    square = Square(6)
    yield square
    del square


@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(3, 4)
    yield rectangle
    del rectangle


@pytest.fixture
def default_circle():
    circle = Circle(7)
    yield circle
    del circle
