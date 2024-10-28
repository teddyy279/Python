def S(n):
    if n == 0: return 0
    return n ** 2 + S(n - 1) 

if _name_ == '_main_':
    n = int(input())
    print(S(n))
