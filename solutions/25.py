# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def main():
    a = 1
    b = 1
    index = 2    
    while True:
        c = a + b
        a = b
        b = c
        index += 1
        if (len(str(c))>=1000):
            print index
            break
    
main()