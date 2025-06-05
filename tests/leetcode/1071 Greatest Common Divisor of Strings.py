"""
1071. Greatest Common Divisor of Strings
Easy
Topics
premium lock icon
Companies
Hint
For two strings s and t, we say "t divides s" if and o
nly if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2,
return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def computer_GCD(len1, len2):
            while len2 != 0:
                temp = len1
                len1 = len2
                len2 = temp % len2
            return len1

        gcd_len = computer_GCD(len(str1), len(str2))

        # temp_GCD = ""
        # for i in range(len(str1)):
        #     temp_GCD = temp_GCD + str1[i]
        #     if len(str1) % len(temp_GCD) != 0 or len(str2) % len(temp_GCD) != 0:
        #         continue
        #     print ("TEMP", temp_GCD)
        #     len1 = len(str1) // len(temp_GCD)
        #     len2 = len(str2) // len(temp_GCD)
        #     if temp_GCD * len1 == str1 and temp_GCD * len2 == str2:
        #         GCD = temp_GCD

        return str1[:gcd_len]

s = Solution()
# a = s.gcdOfStrings("LEET", "CODE")
a = s.gcdOfStrings("ABCABC", "ABC")
print(a)




