def S(n):
    if n == 0: return 0
    if n % 2 == 0:
        return n + S(n - 1)
    return -n + S(n - 1) 

if _name_ == '_main_':
    n = int(input())
    print(S(n))
