from math import *

def is_divisible_11(s):
    sum_odd = 0
    sum_even = 0
    for i in range(len(s)):
        digit = int(s[i])
        if i % 2 == 0:
            sum_odd += digit
        else:
            sum_even += digit
    return abs(sum_even - sum_odd) % 11 == 0

if __name__ == '__main__':
    s = input()
    if is_divisible_11(s):
        print("YES")
    else:
        print("N0")
