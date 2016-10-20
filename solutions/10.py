# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def get_primes(n):
    try:
        _ = int(n)
    except ValueError:
        return []
    
    if (n<2):
        return []

    if (n==2):
        return [2]
    
    primes = [2]
    for i in xrange(3, n+1, 2):        
        prime_flag = 1
        for j in xrange(2, int((i**0.5)+1)):
            if (i%j==0):
                prime_flag = 0
        
        if (prime_flag==1):
            primes.append(i)
    
    return primes

def main():
    primes = get_primes(2000000-1)
    print sum(primes) 

main()
