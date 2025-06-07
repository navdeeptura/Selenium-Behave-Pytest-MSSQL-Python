def fibo(n):
    a = [0, 1]
    if not isinstance(n, (int, float)) or n <= 0:
        return []
    elif int(n) == 1:
        return [0]
    else:
        for i in range(2, int(n)):
            a.append(a[-1] + a[-2])
    return a


def test1_fibo():
    assert fibo(4) == [0, 1, 1, 2]

# Boundary Value Testing
def test_boundary_values():
    assert fibo(1) == [0]
    assert fibo(2) == [0, 1]
    assert fibo(3) == [0, 1, 1]


# Equivalence Partitioning
def test_equivalence_partitioning():
    assert fibo(5) == [0, 1, 1, 2, 3]  # Normal input
    assert fibo(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  # Larger input


# Negative Testing
def test_negative_values():
    assert fibo(-1) == []
    assert fibo(0) == []


# Random Testing
import random


def test_random_values():
    n = random.randint(5, 20)
    result = fibo(n)
    assert len(result) == n
    assert result[-1] == result[-2] + result[-3]  # Checking last value follows Fibonacci pattern


# State Transition Testing
def test_state_transition():
    assert fibo(3) == [0, 1, 1]
    assert fibo(4) == [0, 1, 1, 2]
    assert fibo(5) == [0, 1, 1, 2, 3]


# Performance and Stress Testing
import time


def test_performance_stress():
    start_time = time.time()
    fibo(1000)  # Large input
    assert time.time() - start_time < 1  # Ensuring reasonable execution time

def test_slight_big():
    assert fibo(16) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

# Error Guessing
def test_error_guessing():
    assert fibo("string") == []  # Handling non-numeric input
    assert fibo(None) == []  # Handling None input

def test_float():
    assert fibo(3.5) == [0, 1, 1]  # Handling float input by treating it as an integer
