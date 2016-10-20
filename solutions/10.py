# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math

def get_primes(n):
    try:
        _ = int(n)
    except ValueError:
        return []
    
    if (n<2):
        return []

    if (n==2):
        return [2]
    
    primes = []
    for i in range(2,n+1):
        prime_flag = 1
        for j in range(2, int(math.sqrt(i)+1)):
            if (i%j==0):
                prime_flag = 0
        
        if (prime_flag==1):
            primes.append(i)
    
    return primes

def main():
    primes = get_primes(2000000-1)
    print sum(primes)

main()
