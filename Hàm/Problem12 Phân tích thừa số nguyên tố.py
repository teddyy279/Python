from math import*

def pt(n):
    for i in range(2, isqrt(n) + 1):
        if(n % i == 0):
            mu = 0
            while(n % i == 0):
                mu += 1
                n //= i
            print(i, mu, sep = '^', end = '')
            if(n != 1): print('*', end = '')
    if(n > 1): print(n, 1, sep = '^')

if __name__ == '__main__':
    n = int(input())
    pt(n)
