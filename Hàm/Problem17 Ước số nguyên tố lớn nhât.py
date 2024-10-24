import math

def solve(n):
    res = -1
    for i in range(2, math.isqrt(n) + 1):
        if(n % i == 0):
            res = i
            while(n % i == 0):
                n //= i
    if(n > 1): res = n
    return res

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(solve(n))
