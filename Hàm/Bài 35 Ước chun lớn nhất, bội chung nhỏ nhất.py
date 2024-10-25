from math import*

def gcd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

if _name_ == '_main_':
    a, b = map(int, input().split())
    print(gcd(a, b), lcm(a, b), sep = ' ')
