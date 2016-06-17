
from math import sqrt
from functools import reduce

class Number:
    def __init__(self, number):
        self.number_as_int = number

    def is_even(self):
        if self.number_as_int % 2 == 0:
            return True
        else:
            return False

    def is_odd(self):
        if self.number_as_int % 2 != 0:
            return True
        else:
            return False

    def is_divisible_by(self, number):
        if self.number_as_int % number == 0:
            return True
        else:
            return False

    def is_prime(self):
        start = 2
        end = int(sqrt(self.number_as_int))+1
        for i in range(start, end):
            if self.number_as_int % i == 0:
                return False
            else:
                continue
        return True

    def get_factors(self):
        n = self.number_as_int
        step = 2 if n%2 else 1
        return list(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

    def is_palindrome(self):
        number_as_str = str(self.number_as_int)
        if number_as_str == number_as_str[::-1]:
            return True
        else:
            return False
