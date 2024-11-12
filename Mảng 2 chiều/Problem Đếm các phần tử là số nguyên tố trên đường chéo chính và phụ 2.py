from math import *

def prime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    cnt = 0
    for i in range(n):
        if prime(a[i][i]) or prime(a[i][n - i - 1]): cnt += 1
    print(cnt)
