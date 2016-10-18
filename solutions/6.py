# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def main():
    limit = 100
    sum_of_n = 0
    sum_of_squares = 0
    for i in range(1,limit+1):
        sum_of_n += i
        sum_of_squares += (i**2)

    print sum_of_n**2 - sum_of_squares


main()
