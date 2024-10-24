from math import*

def check(n):
    cnt = 0
    for i in range(1, isqrt(n) + 1):
        if(n % i == 0):
            cnt += 1
            if i != n // i: cnt += 1
    if(n > 1): cnt += 1
    if(cnt % 2 == 0): return False
    return True


if __name__ == '__main__':
    n = int(input())
    if(check(n)): print("NO")
    else: print("YES")
