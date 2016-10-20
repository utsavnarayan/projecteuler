# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def main():
    value = 2**1000

    sum_of_digits = 0
    
    while (value>0):
        sum_of_digits += (value%10)
        value/=10

    print sum_of_digits

main()
