import math

def check(n):
    if n < 2:
        return False
    cnt = 0
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu += 1
                n //= i
                if(mu >= 2): return False
            cnt += 1
    if n > 1:
        cnt += 1
    return cnt == 3

if __name__ == '__main__':
    n = int(input())
    if check(n):
        print(1)
    else:
        print(0)
