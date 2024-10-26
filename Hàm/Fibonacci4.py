from math import*

def prime(n):
    if(n < 2): return False
    for i in range(2, isqrt(n) + 1):
        if(n % i == 0): return False
    return True

def tong(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res

def check(n):
    tmp = tong(n)
    fn1, fn2 = 1, 1
    for i in range(3, 100):
        fn = fn1 + fn2
        fn1, fn2 = fn, fn1
        if(fn == tmp): 
            return True
    return False


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n):
        if(prime(i)):
            if(check(i)): print(i, end = ' ')
    
