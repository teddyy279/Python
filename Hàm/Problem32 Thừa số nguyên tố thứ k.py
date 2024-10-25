import math

def solve(n, k):
    cnt = 0
    for i in range(2, math.isqrt(n)):
        if(n % i == 0):
            while(n % i == 0):
                cnt += 1
                if(cnt == k):
                    return i
                n //= i
    if(n != 1):
        cnt += 1
    if(cnt == k): return n
    return -1

if _name_ == '_main_':
    n, k = map(int, input().split())
    print(solve(n, k))
