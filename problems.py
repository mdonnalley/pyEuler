from Number import Number
import helpers
import cProfile


def problem01():
    '''
    Q: Find the sum of all the multiples of 3 or 5 below 1000.
    A: 233168
    '''
    sum = 0
    for i in range(999, 0, -1):
        num = Number(i)
        if num.is_divisible_by(5) or num.is_divisible_by(3):
            sum += num.number_as_int
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
    n = Number(600851475143)
    factors = n.get_factors()
    largest = 0
    for factor in factors:
        if factor != n.number_as_int and factor > largest and Number(factor).is_prime():
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
            product = Number(product)
            if product.is_palindrome():
                largest = product.number_as_int
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

    grid = []
    grid.append("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08")
    grid.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
    grid.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
    grid.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
    grid.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
    grid.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
    grid.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
    grid.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
    grid.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
    grid.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
    grid.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
    grid.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
    grid.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
    grid.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
    grid.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
    grid.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
    grid.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
    grid.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
    grid.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
    grid.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")

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
    print("----------------------------")

main()

# FOR TESTING:
# cProfile.run('main()')
# cProfile.run('problem10()')
# problem12()
