# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main():
    i = 20
    smallest = 20
    while True:
        flag =0
        for j in range(1,20):
            if (i%j !=0):
                flag=1
                break
        if (flag == 0):
            smallest = i
            break
        i+=1
    print smallest

main()
