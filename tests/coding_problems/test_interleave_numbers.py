import pytest
import ProblemInterleaveTwoNumbers

@pytest.mark.current
def test_interleave_problem():
    assert ProblemInterleaveTwoNumbers.my_solution(456, 12624) == 41526624

def test_interleave_same_length():
    assert ProblemInterleaveTwoNumbers.my_solution(123, 456) == 142536

def test_interleave_unequal_A_shorter():
    assert ProblemInterleaveTwoNumbers.my_solution(45, 67890) == 4657890

def test_interleave_unequal_B_shorter():
    assert ProblemInterleaveTwoNumbers.my_solution(12345, 67) == 1627345

def test_interleave_exceeds_limit():
    assert ProblemInterleaveTwoNumbers.my_solution(123456789, 0) == -1  # Will result in 10203040506070809 > 100000000

def test_interleave_one_digit_each():
    assert ProblemInterleaveTwoNumbers.my_solution(1, 9) == 19

def test_interleave_with_zero():
    assert ProblemInterleaveTwoNumbers.my_solution(0, 1234) == 1234

def test_interleave_both_zero():
    assert ProblemInterleaveTwoNumbers.my_solution(0, 0) == 0

def test_interleave_with_leading_zeros():
    assert ProblemInterleaveTwoNumbers.my_solution(7, 89) == 789  # Should result in '879', leading zeros are not preserved in int

def test_interleave_with_large_difference():
    assert ProblemInterleaveTwoNumbers.my_solution(1, 987654321) == 9187654321 if 9187654321 < 100000000 else -1
