import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def ham2(n):
    cnt = 0
    while n != 0:
        cnt += 1
        n //= 10
    return cnt

def ham3(n):
    cnt = 0
    while n != 0:
        if (n % 10) % 2 == 0:
            cnt += 1
        n //= 10
    return cnt

def ham4(n):
    sum1 = 0
    while n != 0:
        r = n % 10
        if r in [2, 3, 5, 7]:
            sum1 += r
        n //= 10
    return sum1

def reverse(n):
    res = 0
    while n != 0:
        tmp = n % 10
        res = res * 10 + tmp
        n //= 10
    return res

def ham5(n):
    if n < 2:
        return 0
    cnt = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1
            while n % i == 0:
                n //= i
    if n > 1:
        cnt += 1
    return cnt

def ham6(n):
    if n < 2:
        return 0
    res = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res = i
            while n % i == 0:
                n //= i
    if n > 1:
        res = n
    return res

def ham7(n):
    while n != 0:
        if n % 10 == 6:
            return True
        n //= 10
    return False

def ham8(n):
    sum1 = 0
    while n != 0:
        sum1 += n % 10
        n //= 10
    return sum1 % 8 == 0

def ham9(n):
    res = 0
    while n != 0:
        res += math.factorial(n % 10)
        n //= 10
    return res

def ham10(n):
    tmp = n % 10
    check = 1
    while n != 0:
        if tmp != n % 10:
            check = 0
        n //= 10
    return check == 0

def ham11(n):
    tmp = n % 10
    check = 1
    while n != 0:
        if tmp < n % 10:
            check = 0
        n //= 10
    return check == 0

def ham12(n):
    cnt = 0
    original_n = n
    while n != 0:
        cnt += 1
        n //= 10

    n = original_n
    res = 0
    while n != 0:
        res += pow(n % 10, cnt)
        n //= 10
    return res

if __name__ == '__main__':
    n = int(input())
    print(1 if prime(n) else 0)
    print(ham2(n))
    print(ham3(n))
    print(ham4(n))
    print(reverse(n))
    print(ham5(n))
    print(ham6(n))
    print(1 if ham7(n) else 0)
    print(1 if ham8(n) else 0)
    print(ham9(n))
    print(1 if ham10(n) else 0)
    print(1 if ham11(n) else 0)
    print(ham12(n))
