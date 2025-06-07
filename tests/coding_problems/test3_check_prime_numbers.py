import logging
from math import sqrt

def check_prime_number(number):
    sq_num = int(sqrt(number))
    ran = range(1, sq_num, 2)
    count = 0

    if number == 1:
        return False
    if number % 2 == 0:
        return False
    for i in range(1, sq_num, 2):
        if i == 1:
            continue
        if number % i == 0:
            count += 1
    return True if count == 0 else False

def test1():
    num = 12345
    assert check_prime_number(num) == False

def test2():
    num = 1222
    assert check_prime_number(num) == False

def test3():
    num = 12301
    assert check_prime_number(num) == True

def test4():
    num = 29  # Prime number
    assert check_prime_number(num) == True

def test5():
    num = 1  # Not a prime number
    assert check_prime_number(num) == False

def test6():
    num = 1001  # Not a prime number (divisible by 7 and 11)
    assert check_prime_number(num) == False

def test7():
    num = 7919  # Prime number
    assert check_prime_number(num) == True

def test8():
    num = 0  # Not a prime number
    assert check_prime_number(num) == False

def test9():
    num = 104729  # Large prime number
    assert check_prime_number(num) == True