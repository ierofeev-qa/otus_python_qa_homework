import pytest
import math

from src.Figure import Figure


def test_create_figure():
    """Check if creating Figure instance is forbidden"""
    with pytest.raises(TypeError):
        Figure()


def test_create_wrong_triangle(nonexistent_triangle):
    """Check if Triangle class returns None when trying to create a nonexistent triangle"""
    assert nonexistent_triangle is None


def test_triangle_attributes(default_triangle):
    """Check if Triangle instance has attributes 'name', 'area', and 'perimeter"""
    assert all(hasattr(default_triangle, attr) for attr in ['name', 'area', 'perimeter'])


def test_square_attributes(default_square):
    """Check if Square instance has attributes 'name', 'area', and 'perimeter"""
    assert all(hasattr(default_square, attr) for attr in ['name', 'area', 'perimeter'])


def test_rectangle_attributes(default_rectangle):
    """Check if Rectangle instance has attributes 'name', 'area', and 'perimeter"""
    assert all(hasattr(default_rectangle, attr) for attr in ['name', 'area', 'perimeter'])


def test_circle_attributes(default_circle):
    """Check if Circle instance has attributes 'name', 'area', and 'perimeter"""
    assert all(hasattr(default_circle, attr) for attr in ['name', 'area', 'perimeter'])


def test_add_area(default_triangle, default_square, default_rectangle, default_circle):
    """Check if calculation of add_area method is correct"""
    assert math.isclose(default_triangle.area, default_triangle.add_area(default_square) - default_square.area)


def test_add_area_supported_arguments(default_rectangle):
    """Check if add_area method raises ValueError if argument class is not Figure"""
    with pytest.raises(ValueError):
        default_rectangle.add_area(1)
