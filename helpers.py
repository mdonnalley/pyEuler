from Number import Number


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


def filter_list(unfiltered_list, attribute):
    if attribute == 'even':
        return [i for i in unfiltered_list if Number(i).is_even() == True]
    elif attribute == 'odd':
        return [i for i in unfiltered_list if Number(i).is_odd() == True]


def pythagorean(a, b, c):
    return a**2 + b**2 == c**2


def create_txt_of_primes(limit):
    with open('primes.txt', 'w') as outfile:
        outfile.write(str(2) + '\n')
        for num in range(3, limit, 2):
            if Number(num).is_prime():
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

    return primes
