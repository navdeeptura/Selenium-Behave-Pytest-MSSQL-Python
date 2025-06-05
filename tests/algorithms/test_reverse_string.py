import pytest

from algorithms.ReverseString import ReverseString

class TestReverseString:

    reverser = ReverseString()

    @pytest.mark.parametrize("input,expected", [
        ("String", "gnirtS"),
        ("Hello, World!", "!dlroW ,olleH"),
        ("12345", "54321"),
        ("", ""),
        ("a", "a")
    ])
    def test_1(self, input, expected):
        assert self.reverser.reverseUsingStringReverse(input) == expected


    @pytest.mark.parametrize("input,expected", [
        ("String", "gnirtS")
    ])
    def test_2(self, input, expected):
        assert self.reverser.reverseUsingCharLoop(input) == expected