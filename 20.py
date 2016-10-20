# Find the sum of the digits in the number 100!

def main():
    product = 1
    for i in xrange(1,101):
        product *= i

    sum_of_digits = 0
    
    while (product>0):
        sum_of_digits += (product%10)
        product/=10

    print sum_of_digits

main()
