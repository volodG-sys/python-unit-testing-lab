from math_utils import add, divide
import pytest

def test_add():
    assert add(10, 5) == 15

def test_divide_normal():
    assert divide(8, 4) == 2

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
