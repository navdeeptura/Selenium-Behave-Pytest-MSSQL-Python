from pickle import FALSE

import pytest
from sqlalchemy import True_, false

from scripts.algoritms.PalindromeCheck import PalindromeCheck


class TestPalindrome:
    palInstance = PalindromeCheck()


    @pytest.mark.parametrize("string,expected", [
        ("Racecar", True),
        ("racecar", True),
        ("Navdeep", False)
    ])
    def testValidCaseUpper(self, string, expected):
        assert self.palInstance.verifyPalindrome(string) == expected