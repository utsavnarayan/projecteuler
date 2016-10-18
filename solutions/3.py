# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143
import math

def brute_force():
    a = 600851475143
    largest_prime_factor = 0
    i=(600851475143/2)+1
    while (i>2):
        i-=1
        # check if its a factor
        if (a%i==0):
            # check if its prime
            flag = 0
            for j in range(2,int(math.sqrt(i))+1):                
                if (i%j==0):                    
                    flag+=1
                    break
            if (flag == 0 and i>largest_prime_factor):
                largest_prime_factor = i
                break

    print largest_prime_factor

brute_force()
