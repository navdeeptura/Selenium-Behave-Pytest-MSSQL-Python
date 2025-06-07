def swap_2_number(A, B):
    A = A + B
    B = A - B
    A = A - B
    return (A, B)

def swap_with_temp(A, B):
    temp = A + B
    A = temp - A
    B = temp - B
    return (A, B)

def test_swap_number():
    assert swap_2_number(1 , 2) == (2, 1)

def test_swap_big():
    assert swap_2_number(1122, 33445) == (33445, 1122)

def test_swap_temp1():
    assert swap_with_temp(1122, 33445) == (33445, 1122)

# Boundary Value Testing
def test_swap_boundary():
    assert swap_2_number(0, 1) == (1, 0)
    assert swap_2_number(-1, 0) == (0, -1)

# Equivalence Partitioning
def test_swap_equivalence_positive():
    assert swap_2_number(10, 20) == (20, 10)

def test_swap_equivalence_negative():
    assert swap_2_number(-10, -20) == (-20, -10)

def test_swap_equivalence_mixed():
    assert swap_2_number(-5, 5) == (5, -5)

# Negative Testing
def test_swap_invalid_type():
    try:
        swap_2_number("a", "b")  # Invalid types
    except TypeError:
        assert True

# Random Testing
import random
def test_swap_random():
    a, b = random.randint(-1000, 1000), random.randint(-1000, 1000)
    assert swap_2_number(a, b) == (b, a)

# State Transition Testing
def test_swap_state_transition():
    result = swap_2_number(0, 1)
    assert result == (1, 0)
    assert swap_2_number(*result) == (0, 1)

# Performance and Stress Testing
def test_swap_large_numbers():
    assert swap_2_number(10**6, 10**7) == (10**7, 10**6)

def test_swap_many_calls():
    for _ in range(100000):
        assert swap_2_number(1, 2) == (2, 1)

# Error Guessing
def test_swap_zero():
    assert swap_2_number(0, 0) == (0, 0)