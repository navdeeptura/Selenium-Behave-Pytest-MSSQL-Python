import pytest

from ProblemFindMaximumValidTime import max_time

@pytest.mark.parametrize(
    "digits, time",
    [
        ([1, 9, 2, 3], "23:19"),
        ([5, 5, 5, 5], "NOT POSSIBLE"),
        ([2, 3, 5, 9], "23:59")
    ]
)

def test_max_time(digits, time):
    assert max_time(digits) == time

"""
def test_valid_max_time_case():
    assert max_time([1, 9, 2, 3]) == "23:19"

def test_all_same_digits_invalid():
    assert max_time([5, 5, 5, 5]) == "NOT POSSIBLE"

def test_multiple_valid_times():
    assert max_time([2, 3, 5, 9]) == "23:59"  # Highest valid time

def test_earliest_possible_valid_time():
    assert max_time([0, 0, 0, 0]) == "00:00"

def test_with_valid_but_low_time():
    assert max_time([0, 1, 2, 3]) == "23:10"

def test_invalid_due_to_minutes():
    assert max_time([2, 4, 6, 7]) == "NOT POSSIBLE"  # All minute combinations are invalid

def test_invalid_due_to_hours():
    assert max_time([2, 9, 5, 9]) == "NOT POSSIBLE"  # All hour combinations exceed 24

def test_multiple_same_digits_valid():
    assert max_time([1, 2, 1, 2]) == "22:11"

def test_valid_low_time():
    assert max_time([0, 0, 1, 2]) == "21:00"

def test_non_max_but_valid():
    assert max_time([1, 2, 3, 4]) == "23:41"
"""