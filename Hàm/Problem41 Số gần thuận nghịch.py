from math import*

def check_palindromic_number(n):
    tmp = n
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == tmp

def check(n):
    last = n % 10
    sum1 = 0
    n //= 10
    while n >= 10:
        sum1 += n % 10
        n //= 10
    if((last * 2 == n) or (n * 2 == last)) and check_palindromic_number(n): return True
    return False

if __name__ == '__main__':
    n = int(input())
    if(check(n)): print("YES")
    else: print("NO")
