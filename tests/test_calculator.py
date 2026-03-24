import pytest
from app import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_soustraction():
    assert calculator.soustraction(5, 3) == 2
    assert calculator.soustraction(1, 1) == 0
    assert calculator.soustraction(0, 0) == 0