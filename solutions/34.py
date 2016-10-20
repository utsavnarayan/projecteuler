# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def factorial(n):
    fact = 1
    while (n>0):
        fact*=n
        n-=1
    return fact

def main():
    magic_sum = 0
    for i in range(3,10000000):        
        sum_required, num = i, i
        while num>0:
            sum_required -= factorial(num%10)
            num/=10
        if (sum_required == 0):
            print i
            magic_sum += i

    print magic_sum

main()
