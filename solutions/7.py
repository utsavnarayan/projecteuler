# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def is_prime(n):
    if n==2:
        return True

    for i in range(2,int(math.sqrt(n)+1)):
        if (n%i==0):
            return False
    return True


def main():
    limit = 10001
    i = 2
    while limit>0:
        if is_prime(i):
            print i
            limit-=1
        i+=1
        

main()
