from math import*

def check(n):
    for i in range(0, n // 111 + 1):
        if (n - (i * 111)) % 11 == 0:
            return True
    return False

if _name_ == '_main_':
    n = int(input())
    if(check(n)): print("YES")
    else: print("NO")
