import helpers
import problem_setup


def problem01():
    """
    Q: Find the sum of all the multiples of 3 or 5 below 1000.
    A: 233168
    """
    total_sum = 0
    for num in range(999, 0, -1):
        if helpers.is_divisible_by(num, 5) or helpers.is_divisible_by(num, 3):
            total_sum += num

    return total_sum


def problem02():
    """
    Q: By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    A: 4613732
    """

    fib_sequence = helpers.generate_fibonacci_sequence(limit=4000000)
    fib_sequence_filtered = helpers.filter_list(fib_sequence, 'even')
    fib_sequence_added = helpers.add_all(fib_sequence_filtered)

    return fib_sequence_added


def problem03():
    """
    Q: What is the largest prime factor of the number 600851475143?
    A: 6857
    """
    n = 600851475143
    factors = helpers.get_factors(n)
    largest = 0
    for factor in factors:
        if factor != n and factor > largest and helpers.is_prime(factor):
            largest = factor

    return largest


def problem04():
    """
    Q: Find the largest palindrome made from the product of two 3-digit numbers.
    A: 906609
    """

    largest = 0
    for num in range(900, 999):
        for n in range(900, 999):
            product = num*n
            if product < largest:
                continue
            if helpers.is_palindrome(product):
                largest = product

    return largest


def problem05():
    """
    Q: What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    A: 232792560
    """

    a = False
    # 2520 is the least common multiple of 2,3,4 and 10
    # the answer has to be a multiple of 2520
    num = 2520
    while not a:
        for i in range(19, 0, -1):
            if num % i == 0:
                a = True
            else:
                a = False
                break

        if a:
            continue
        else:
            num += 2520

    return num


def problem06():
    """
    Q: Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    A: 25164150
    """

    sum_of_squares = 0
    sum_of_numbers = 0
    for num in range(1, 101):
        sum_of_squares += num ** 2
        sum_of_numbers += num
    square_of_sum = sum_of_numbers ** 2

    return square_of_sum - sum_of_squares


def problem07():
    """
    Q: What is the 10001st prime number?
    A: 104743
    """

    count = 10001
    primes = helpers.get_set_of_primes(parameter_type='count', value=count)

    return max(primes)


def problem08():
    """
    Q: Find the thirteen adjacent digits in the 1000-digit number that have the
    greatest product. What is the value of this product?
    A: 23514624000
    """

    digits = problem_setup.problem08_setup()

    end = len(digits) - 13
    max_product = 0
    for d in range(0, end):
        product = 1
        for i in range(0, 13):
            product *= int(digits[d+i])
            if product > max_product:
                max_product = product

    return max_product


def problem09():
    """
    Q: There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    A: 31875000
    """

    from math import sqrt
    for a in range(5, 1000, 5):
        for b in range(5, 1000, 5):
            c = 1000 - (a + b)
            if c < b:
                continue
            elif sqrt(a**2 + b**2) % 1 != 0:
                continue
            else:
                if helpers.pythagorean(a, b, c):
                    return a*b*c


def problem10():
    """
    Q: Find the sum of all the primes below two million.
    A: 142913828922
    """

    limit = 2000001
    primes = helpers.get_set_of_primes(parameter_type='limit', value=limit)
    sum_of_primes = helpers.add_all(primes)

    return sum_of_primes


def problem11():
    """
    Q: What is the greatest product of four adjacent numbers in the same
    direction (up, down, left, right, or diagonally) in the 20x20 grid?
    A : 70600674
    """

    grid = problem_setup.problem11_setup()
    grid = [i.split() for i in grid]
    grid = [[int(j) for j in i] for i in grid]

    max_product = 0

    for i in range(20):
        for j in range(16):
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if product > max_product:
                max_product = product
            product = grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i]
            if product > max_product:
                max_product = product

    for i in range(16):
        for j in range(16):
            product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if product > max_product:
                max_product = product
    for i in range(3, 20):
        for j in range(16):
            product = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            if product > max_product:
                max_product = product

    return max_product


def problem12():
    """
    Q: What is the value of the first triangle number to have over five hundred
    divisors?
    A: 76576500
    """

    primes = helpers.get_set_of_primes(parameter_type='all', value=None)
    index = 25
    number_of_divisors = 0
    triangle_number = 0
    while number_of_divisors < 500:
        index += 25
        triangle_number = helpers.triangular_number(index)
        if triangle_number % 2 != 0:
            continue
        prime_factors = helpers.get_prime_factors(triangle_number, primes)
        number_of_divisors = helpers.get_number_of_divisors(prime_factors)

    return int(triangle_number)


def problem13():
    """
    Q: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    A: 5537376230
    """
    numbers = problem_setup.problem13_setup()
    total = helpers.add_all(numbers)
    first_10_digits = str(total)[:10]

    return first_10_digits


def problem14():
    """
    Q: Which starting number, under one million, produces the longest chain?
    A: 837799
    """

    largest = {'start': 0, 'count': 0}
    cache = {}
    for num in range(0, 1000000):
        count = 1
        start = num
        while num > 1:
            if num in cache:
                count += cache[num] - 1
                break
            if num % 2 == 0:
                num /= 2
            else:
                num = (3 * num) + 1
            count += 1

        if count > largest['count']:
            largest['count'] = count
            largest['start'] = start

        cache[start] = count

    return largest['start']


def problem15():
    """
    Q: Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are
    exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?
    A: 137846528820
    """
    grid = [1] * 20
    for i in range(20):
        for j in range(i):
            grid[j] += grid[j-1]
        grid[i] = 2 * grid[i-1]

    return grid[20 - 1]


def problem16():
    """
    Q: What is the sum of the digits of the number 2^1000?
    A: 1366
    """
    power_digits = str(2**1000)
    total_sum = 0
    for digit in power_digits:
        total_sum += int(digit)
    return total_sum

def problem17():
    """
    Q: If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?
    A:
    """
    special_cases = {
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }
    all_characters = ''
    for number in range(1, 1001):
        number = str(number)
        if number in special_cases:
            full_number = special_cases[number]
        else:
            if number[-2:] in special_cases:
                full_number = special_cases[number[-2:]]
                number_to_iterate = number[0] + '00'
            else:
                full_number = ''
                number_to_iterate = number

            idx = len(number_to_iterate)
            for digit in number_to_iterate:
                full_number += convert_to_characters(digit, idx)
                idx -= 1

        print(full_number)
        all_characters += full_number
    return len(all_characters)


def convert_to_characters(num, index):

    singles = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    doubles = {
        '0': '',
        '1': 'ten',
        '2': 'twenty',
        '3': 'thirty',
        '4': 'fourty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }

    triples = {
        '0': '',
        '1': 'onehundredand',
        '2': 'twohundredand',
        '3': 'threehundredand',
        '4': 'fourhundredand',
        '5': 'fivehundredand',
        '6': 'sixhundredand',
        '7': 'sevenhundredand',
        '8': 'eighthundredand',
        '9': 'ninehundredand'
    }

    quad = {
        '0': '',
        '1': 'onethousand'
    }

    if index == 1:
        return singles[num]
    elif index == 2:
        return doubles[num]
    elif index == 3:
        return triples[num]
    elif index == 4:
        return quad[num]
    else:
        return ''

def main():
    print("------ Project Euler ------")
    print(" Problem 01:", problem01())
    print(" Problem 02:", problem02())
    print(" Problem 03:", problem03())
    print(" Problem 04:", problem04())
    print(" Problem 05:", problem05())
    print(" Problem 06:", problem06())
    print(" Problem 07:", problem07())
    print(" Problem 08:", problem08())
    print(" Problem 09:", problem09())
    print(" Problem 10:", problem10())
    print(" Problem 11:", problem11())
    print(" Problem 12:", problem12())
    print(" Problem 13:", problem13())
    print(" Problem 14:", problem14())
    print(" Problem 15:", problem15())
    print(" Problem 16:", problem16())
    print("----------------------------")


def test_problem(number, profile=False):
    if number == 'main()':
        problem_string = number
    else:
        problem_string = 'problem{number}()'.format(number=number)

    if profile:
        import cProfile
        cProfile.run(problem_string)
    else:
        print(eval(problem_string))


# main()
test_problem('17', False)
