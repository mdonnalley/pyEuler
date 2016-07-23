from math import sqrt
from functools import reduce
from bisect import bisect_right

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
    return (number % 2 == 0)


def is_odd(number):
    return (number % 2 != 0)


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


def is_whole(number):
    if number % 1 == 0:
        return True
    else:
        return False


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
            primes_txt = list(map(int, infile.read().splitlines()))
            primes = set(primes_txt[0:value])
        elif parameter_type == 'all':
            primes = list(map(int, infile.read().splitlines()))

    return primes


def find_nearest_prime(primes, x):
    'Find leftmost value greater than x'
    i = bisect_right(primes, x)
    if i != len(primes):
        return primes[i]
    raise ValueError


def get_prime_factors(number, primes):
    factors = []
    square_root = int(sqrt(number))
    end = find_nearest_prime(primes, square_root)
    end = primes.index(end)
    subset = primes[0:end]
    for prime in subset:
        if number % prime != 0:
            continue

        quotient = number/prime

        while quotient % 1 == 0:
            if number % quotient == 0:
                factors.append(prime)
            quotient /= prime

    return factors


def consolidate_prime_factors(factors):
    output = dict()
    for factor in factors:
        output[str(factor)] = factors.count(factor)
    return output


def get_number_of_divisors(prime_factors):
    prime_factors_dict = consolidate_prime_factors(prime_factors)
    number_of_divisors = 1
    for key in prime_factors_dict:
        count = prime_factors_dict[key] + 1
        number_of_divisors *= count
    return number_of_divisors


def triangular_number(number):
    return (number * (number + 1)) / 2
