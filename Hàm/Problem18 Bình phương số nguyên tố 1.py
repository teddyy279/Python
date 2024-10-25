from math import isqrt

def solve(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu += 1
                n //= i  # Corrected this line
            if mu >= 2:
                return True
    return False

if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if solve(i):
            print(i, end=' ')
