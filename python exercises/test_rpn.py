from rpn import evaluate
from math import isclose
from pytest import approx

def test_single_integer():
    assert evaluate("5") == 5.0
    
def test_single_float():
    assert isclose(evaluate("3.0"), 3.0)

def test_negative_number():
    assert evaluate("-7") == -7.0

def test_two_digit_number():
    assert evaluate("12") == 12.0 

def test_addition():
    assert evaluate("3 5 +") == 8.0

def test_subtraction():
    assert evaluate("7 2 -") == 5.0

def test_multiplication():
    assert evaluate("2 2 *") == 4.0

def test_division():
    assert isclose(evaluate("300 15 /"), 300 / 15)

def test_three_numbers_two_operators():
    assert evaluate("2 3 4 - +") == 1.0
    
def test_two_number_an_operator_third_number_another_operator():
    assert evaluate("32 15 / 28 *") == approx((32 / 15) * 28)
                   
                   
    
    