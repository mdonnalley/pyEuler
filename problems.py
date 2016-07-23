import helpers
import problem_setup
import cProfile


def problem01():
    '''
    Q: Find the sum of all the multiples of 3 or 5 below 1000.
    A: 233168
    '''
    sum = 0
    for num in range(999, 0, -1):
        if helpers.is_divisible_by(num, 5) or helpers.is_divisible_by(num, 3):
            sum += num
    # print(sum)
    return sum


def problem02():
    '''
    Q: By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    A: 4613732
    '''

    fib_sequence = helpers.generate_fibonacci_sequence(limit=4000000)
    fib_sequence_filtered = helpers.filter_list(fib_sequence, 'even')
    fib_sequence_added = helpers.add_all(fib_sequence_filtered)
    # print(fib_sequence_added)
    return fib_sequence_added


def problem03():
    '''
    Q: What is the largest prime factor of the number 600851475143?
    A: 6857
    '''
    n = 600851475143
    factors = helpers.get_factors(n)
    largest = 0
    for factor in factors:
        if factor != n and factor > largest and helpers.is_prime(factor):
            largest = factor
    # print(largest)
    return largest


def problem04():
    '''
    Q: Find the largest palindrome made from the product of two 3-digit numbers.
    A: 906609
    '''

    largest = 0
    for num in range(900,999):
        for n in range(900,999):
            product = num*n
            if product < largest:
                continue
            if helpers.is_palindrome(product):
                largest = product
    # print(largest)
    return largest


def problem05():
    '''
    Q: What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    A: 232792560
    '''

    a = False
    # 2520 is the least common multiple of 2,3,4 and 10
    # the answer has to be a multiple of 2520
    num = 2520
    while a == False:
        for i in range(19, 0, -1):
            if num % i == 0:
                a = True
            else:
                a = False
                break

        if a == True:
            continue
        else:
            num += 2520

    # print(num)
    return num


def problem06():
    '''
    Q: Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    A: 25164150
    '''

    sum_of_squares = 0
    sum_of_numbers = 0
    for num in range(1, 101):
        sum_of_squares += num ** 2
        sum_of_numbers += num
    square_of_sum = sum_of_numbers ** 2
    # print(square_of_sum - sum_of_squares)
    return square_of_sum - sum_of_squares


def problem07():
    '''
    Q: What is the 10001st prime number?
    A: 104743
    '''

    count = 10001
    primes = helpers.get_set_of_primes(parameter_type='count', value=count)
    # print(max(primes))
    return max(primes)


def problem08():
    '''
    Q: Find the thirteen adjacent digits in the 1000-digit number that have the
    greatest product. What is the value of this product?
    A: 23514624000
    '''

    digits = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

    end = len(digits) - 13
    max_product = 0
    for d in range(0, end):
        product = 1
        for i in range(0,13):
            product *= int(digits[d+i])
            if product > max_product:
                max_product = product
    # print(max_product)
    return max_product


def problem09():
    '''
    Q: There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    A: 31875000
    '''

    from math import sqrt
    for a in range(5,1000,5):
        for b in range(5,1000,5):
            c = 1000 - (a + b)
            if c < b:
                continue
            elif sqrt(a**2 + b**2) % 1 != 0:
                continue
            else:
                if helpers.pythagorean(a, b, c):
                    # print(a*b*c)
                    return a*b*c


def problem10():
    '''
    Q: Find the sum of all the primes below two million.
    A: 142913828922
    '''

    limit = 2000001
    primes = helpers.get_set_of_primes(parameter_type='limit', value=limit)
    sum_of_primes = helpers.add_all(primes)
    # print(sum_of_primes)
    return sum_of_primes


def problem11():
    '''
    Q: What is the greatest product of four adjacent numbers in the same
    direction (up, down, left, right, or diagonally) in the 20×20 grid?
    A: 70600674
    '''

    grid = problem_setup.problem11()
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
    for i in range(3,20):
        for j in range(16):
            product = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            if product > max_product:
                max_product = product

    # print(max_product)
    return max_product


def problem12():
    '''
    Q: What is the value of the first triangle number to have over five hundred
    divisors?
    A: 76576500
    '''

    primes = helpers.get_set_of_primes(parameter_type='all', value=None)
    index = 25
    number_of_divisors = 0
    while number_of_divisors < 500:
        index += 25
        triangle_number = helpers.triangular_number(index)
        if triangle_number % 2 != 0:
            continue
        prime_factors = helpers.get_prime_factors(triangle_number, primes)
        number_of_divisors = helpers.get_number_of_divisors(prime_factors)

    # print(triangle_number)
    return int(triangle_number)


def problem13():
    '''
    Q: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    A: 5537376230
    '''
    numbers = problem_setup.problem13()
    sum = helpers.add_all(numbers)
    first_10_digits = str(sum)[:10]

    # print(first_10_digits])
    return first_10_digits


def problem14():
    '''
    Q: Which starting number, under one million, produces the longest chain?
    A: 837799
    '''
    largest = {'start': 0, 'count': 0}
    cache = {}
    for num in range(0,1000000):
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

    # print(largest['start'])
    return largest['start']



def main():
    print("------ Project Euler ------")
    print(" Problem  01:", problem01())
    print(" Problem  02:", problem02())
    print(" Problem  03:", problem03())
    print(" Problem  04:", problem04())
    print(" Problem  05:", problem05())
    print(" Problem  06:", problem06())
    print(" Problem  07:", problem07())
    print(" Problem  08:", problem08())
    print(" Problem  09:", problem09())
    print(" Problem  10:", problem10())
    print(" Problem  11:", problem11())
    print(" Problem  12:", problem12())
    print(" Problem  13:", problem13())
    print(" Problem  14:", problem14())
    print("----------------------------")


main()

# FOR TESTING:
# cProfile.run('main()')
# cProfile.run('problem14()')
# problem14()
