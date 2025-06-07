def sum_of_array(lis):

    if not isinstance(lis, list):
        return 0
    c = 0
    for i in lis:
        if isinstance(i, int):
            c = c+i
    return c

def test_sum():
    assert sum_of_array([1,2]) == 3

# Test Suite for sum_of_array function

# Boundary Value Testing
def test_boundary_values():
    assert sum_of_array([0]) == 0  # Minimum input
    assert sum_of_array([0, 0]) == 0  # Edge case with zeros
    assert sum_of_array([-1, 1]) == 0  # Edge case at extremes

# Equivalence Partitioning
def test_equivalence_partitioning():
    assert sum_of_array([1, 2, 3]) == 6  # Positive numbers
    assert sum_of_array([-1, -2, -3]) == -6  # Negative numbers
    assert sum_of_array([0, 0, 0]) == 0  # Neutral case (zeros)

# Negative Testing
def test_negative_values():
    assert sum_of_array([]) == 0  # Empty list
    assert sum_of_array(None) == 0  # None input (assuming your function handles this gracefully)
    assert sum_of_array("string") == 0  # Invalid input type (string)

# Random Testing
import random
def test_random_values():
    lst = [random.randint(-10, 10) for _ in range(10)]
    assert sum_of_array(lst) == sum(lst)  # Compare with Python's built-in sum()

# State Transition Testing
def test_state_transition():
    assert sum_of_array([0, 1]) == 1  # Transition from neutral to positive
    assert sum_of_array([1, -1]) == 0  # Transition from positive to neutral
    assert sum_of_array([-1, -2]) == -3  # Transition from negative to further negative

# Performance and Stress Testing
import time
def test_performance_stress():
    large_list = [i for i in range(1000000)]  # Large input
    start_time = time.time()
    assert sum_of_array(large_list) == sum(large_list)  # Verify correctness
    assert time.time() - start_time < 1  # Ensure reasonable execution time

# Error Guessing
def test_error_guessing():
    assert sum_of_array([1, None, 3]) == 4  # Handling mixed valid/invalid input
    assert sum_of_array([float('nan'), 1]) == 1  # Handling NaN (ignoring it)
