# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def main():
    num = 1001
    diag_sum = 1 # Sum of series 1 3 5 7 9 13 17 21 25 31 37 43 49
    terms_to_skip = 2 # will get increased by 2 in outer circles
    terms_to_select = 4
    value = 1
    while (value < (num**2)+1):        
        value += terms_to_skip
        diag_sum += value
        terms_to_select -= 1
        if (terms_to_select == 0):
            terms_to_skip += 2
            terms_to_select = 4
    
    print diag_sum - value # remove the last term that got added

main()
