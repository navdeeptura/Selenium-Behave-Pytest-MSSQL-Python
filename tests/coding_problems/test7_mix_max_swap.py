def man_mix(li):
    # maxi = max(li)
    # mini = min(li)
    # return [maxi, mini]
    if not isinstance(li, list) or len(li) <= 0:
        return []
    maxi = li[0]
    mini = li[0]
    for i in li:
        if i is None:
            pass
        elif isinstance(i, int):
            if maxi < i: maxi = i
            if mini > i: mini = i
    return [maxi, mini]



def test1_li():
    assert man_mix([5,3,7,1]) == [7, 1]

# Test Suite for man_mix function

# Boundary Value Testing
def test_boundary_values():
    assert man_mix([1]) == [1, 1]  # Single element, max and min are the same
    assert man_mix([5, 5]) == [5, 5]  # Two identical elements
    assert man_mix([0, -1, 1]) == [1, -1]  # Smallest range including zero

# Equivalence Partitioning
def test_equivalence_partitioning():
    assert man_mix([5, 3, 7, 1]) == [7, 1]  # Distinct positive integers
    assert man_mix([-5, -3, -7, -1]) == [-1, -7]  # Distinct negative integers
    assert man_mix([0, 0, 0]) == [0, 0]  # Identical zero values

# Negative Testing
def test_negative_values():
    assert man_mix([]) == []  # Empty list
    assert man_mix(None) == []  # None input (assuming this behavior)
    assert man_mix("string") == []  # Invalid type input

# Random Testing
import random
def test_random_values():
    lst = [random.randint(-100, 100) for _ in range(10)]
    assert man_mix(lst) == [max(lst), min(lst)]  # Compare function output to expected results

# State Transition Testing
def test_state_transition():
    assert man_mix([1, 2, 3]) == [3, 1]  # Sorted ascending list
    assert man_mix([3, 2, 1]) == [3, 1]  # Sorted descending list
    assert man_mix([3, 1, 2]) == [3, 1]  # Mixed order

# Performance and Stress Testing
import time
def test_performance_stress():
    large_list = [random.randint(-1000000, 1000000) for _ in range(1000000)]  # Large input
    start_time = time.time()
    max_min = man_mix(large_list)  # Execute the function
    assert max_min == [max(large_list), min(large_list)]  # Verify correctness
    assert time.time() - start_time < 1  # Ensure execution within 1 second


def swap(li):
    to_be_first = li[-1]
    li[-1] = li[0]
    li[0] = to_be_first
    return li

def test1_swap1():
    assert swap([2, 4, 6, 6]) == [6, 4, 6, 2]