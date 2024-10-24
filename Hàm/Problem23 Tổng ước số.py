from math import*

def solve(n):
    res = 0
    for i in range(1, isqrt(n) + 1):
        if(n % i == 0):
            res += i
            if(i != n // i): res += n // i
    return res

if __name__ == '__main__':
    n = int(input())
    print(solve(n))
