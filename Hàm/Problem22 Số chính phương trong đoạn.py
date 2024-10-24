from math import*

def cp(n):
    can = isqrt(n)
    return can * can == n

if __name__ == '__main__':
    a, b = map(int, input().split())
    can1, can2 = isqrt(a), isqrt(b)
    if(can1 * can1 != a): can1 += 1
    cnt = 0
    for i in range(can1, can2 + 1):
        if(cp(i * i)): cnt += 1
    print(cnt)
