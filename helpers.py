from math import sqrt
from functools import reduce


def generate_fibonacci_sequence(limit):
    sequence = [1, 2]
    while sequence[-1] < limit:
        last = len(sequence) - 1
        next_num = sequence[last] + sequence[last-1]
        sequence.append(next_num)
    if sequence[-1] > limit:
        del sequence[-1]
    return sequence


def add_all(list_of_numbers):
    result = 0
    for num in list_of_numbers:
        result += num
    return result


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False


def is_divisible_by(a, b):
    if a % b == 0:
        return True
    else:
        return False


def is_prime(number):
    start = 2
    end = int(sqrt(number))+1
    for i in range(start, end):
        if number % i == 0:
            return False
        else:
            continue
    return True


def is_palindrome(number):
    number_as_str = str(number)
    if number_as_str == number_as_str[::-1]:
        return True
    else:
        return False


def get_factors(n):
    step = 2 if n%2 else 1
    return list(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


def filter_list(unfiltered_list, attribute):
    if attribute == 'even':
        return [i for i in unfiltered_list if is_even(i) == True]
    elif attribute == 'odd':
        return [i for i in unfiltered_list if is_odd(i) == True]


def pythagorean(a, b, c):
    return a**2 + b**2 == c**2


def create_txt_of_primes(limit):
    with open('primes.txt', 'w') as outfile:
        outfile.write(str(2) + '\n')
        for num in range(3, limit, 2):
            if is_prime(num):
                outfile.write(str(num) + '\n')


def get_set_of_primes(parameter_type, value):
    with open('primes.txt') as infile:
        if parameter_type == 'limit':
            primes_txt = infile.readlines()
            primes = set()
            for prime in primes_txt:
                prime = int(prime)
                if prime <= value:
                    primes.add(prime)
        elif parameter_type == 'count':
            f = infile.read().splitlines()
            primes_txt = [int(line) for line in f]
            primes = set(primes_txt[0:value])
        elif parameter_type = 'none':
            primes = set(infile.readlines())

    return primes
