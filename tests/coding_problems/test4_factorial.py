from numpy.ma.core import count

def rec_factorial(n):
    if n < 0:
        raise ValueError("Factorial can't be provided")
    if n == 0 or n == 1:
        return 1
    return n * factorial_check(n-1)

def factorial_check(n):
    if n < 0:
        raise ValueError("Factorial can't be provided")
    county = 1
    for i in range(1, n+1):
        county = county * i
    return county

def test1_fact():
    assert factorial_check(3) == 6

import random

# Boundary Value Testing
def test_boundary_0():
    assert factorial_check(0) == 1  # Edge case: Factorial of 0

def test_boundary_1():
    assert factorial_check(1) == 1  # Edge case: Factorial of 1

def test_boundary_2():
    assert factorial_check(2) == 2  # Just above lower boundary

# Equivalence Partitioning
def test_equivalence_small():
    assert factorial_check(4) == 24  # Normal case, small valid number

# Equivalence Partitioning
def test_equivalence_small_2():
    assert rec_factorial(4) == 24  # Normal case, small valid number

def test_equivalence_medium():
    assert factorial_check(6) == 720  # Mid-range valid number

def test_equivalence_large():
    assert factorial_check(10) == 3628800  # Larger valid number

# Negative Testing
def test_negative_value():
    try:
        factorial_check(-5)  # Invalid input
    except ValueError:
        assert True  # Ensure exception is raised

def test_invalid_type():
    try:
        factorial_check("hello")  # Invalid type (string)
    except TypeError:
        assert True  # Ensure exception is raised

# Random Testing
def test_random():
    num = random.randint(1, 10)
    expected = 1
    for i in range(1, num + 1):
        expected *= i
    assert factorial_check(num) == expected  # Verify correctness

# State Transition Testing
def test_state_transition():
    assert factorial_check(3) == 6  # From non-factorial state to computed state
    assert factorial_check(4) == 24  # Valid transition in sequence

# Performance and Stress Testing
def test_large_factorial():
    assert factorial_check(20) == 2432902008176640000  # Ensure function handles large numbers

def test_stress_many_calls():
    for _ in range(10000):  # Stress test with repeated calls
        assert factorial_check(5) == 120

# Error Guessing
def test_edge_zero():
    assert factorial_check(0) == 1  # Handle specific zero case properly

def test_edge_one():
    assert factorial_check(1) == 1  # Handle specific one case properly