from math import*

def check1(n):
    original = n
    res = 0 
    while n != 0:
        tmp = n % 10
        res = res * 10 + tmp
        n //= 10
    return res == original

def check2(n):
    if(n < 2): return False
    cnt = 0
    for i in range(2, isqrt(n) + 1):
        if(n % i == 0):
            cnt += 1
            while(n % i == 0):
                n //= i
    if(n > 1): cnt += 1
    return cnt >= 3

if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if(check1(i) and check2(i)): print(i, end = ' ')
