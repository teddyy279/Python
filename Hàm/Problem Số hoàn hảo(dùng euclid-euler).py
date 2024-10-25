from math import*

def prime(n):
    if(n < 2): return False
    for i in range(2, isqrt(n) + 1):
        if(n % i == 0): return False
    return True

def Euclid_Euler(n):
    for p in range(2, 35):
        if(prime(p)):
            if(prime(2 ** p - 1)):
                if((2 * (p - 1)) * (2 * p - 1)) == n: 
                    return True
    return False

if _name_ == '_main_':
    n = int(input())
    if(Euclid_Euler(n)): print("YES")
    else: print("NO")
