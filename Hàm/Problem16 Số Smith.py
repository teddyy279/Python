from math import isqrt

def digit_sum(n):
    sum1 = 0
    while n != 0:
        sum1 += n % 10
        n //= 10
    return sum1

def check(n):
    sum1 = digit_sum(n)
    sum2 = 0
    tmp = n
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                sum2 += i
                n //= i
    if tmp == n:
        return False
    if n > 1:
        sum2 += digit_sum(n)
    return sum1 == sum2

if __name__ == '__main__':
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")
