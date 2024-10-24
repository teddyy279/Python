from math import*

def check1(n):
    if(n < 2): return False
    for i in range(2, isqrt(n) + 1):
        if(n % i == 0): return False
    return True

def check2(n):
    sum1 = 0
    while n != 0:
        r = n % 10
        if(r == 2 or r == 3 or r == 5 or r == 7):
            sum1 += r
        else: return False
        n //= 10
    if(check1(sum1)): return True
    return False

if __name__ == '__main__':
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b + 1):
        if(check1(i) and check2(i)): cnt += 1
    print(cnt)
