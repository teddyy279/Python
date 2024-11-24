from math import*

def prime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    sum_digit = 0
    for i in range(len(s)):
        digit = int(s[i])
        if prime(digit):
            sum_digit += digit
        else:
            return False
    return prime(sum_digit)        

if __name__ == '__main__':
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")
