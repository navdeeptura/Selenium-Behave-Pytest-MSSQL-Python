"""Problem 1: Interleaving Two Numbers
Description: Given two integers A and 𝐵, interleave their digits alternately.
If one number has more digits, append the remaining digits at the end.
If the resulting number exceeds 100,000,000, return -1.
Solution (already provided by you, slightly optimized):
"""
from itertools import zip_longest


# my code
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#from measure_latency import measure_latency

#w@measure_latency
def my_solution(A, B):
    # Implement your solution here
    a, b = str(A), str(B)
    result = []
    x = 0

    while x < len(a) and x < len(b):
        result.append(a[x])
        result.append(b[x])
        x += 1

    result.extend(a[x:])
    result.extend(b[x:])

    num = int("".join(result))

    return num if num < 100000000 else -1

A, B = 456, 12624
print (f"The Output is : {my_solution(A,B)}")