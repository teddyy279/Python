from math import*

def check(n):
    tmp = sqrt(n)
    return tmp * tmp == n

if __name__ == '__main__':
    n = int(input())
    if(check(n)): print("YES")
    else: print("NO")
