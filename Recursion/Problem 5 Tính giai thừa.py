def Factorial(n):
    if n == 0: return 1
    return n * Factorial(n - 1)

if _name_ == '_main_':
    n = int(input())
    print(Factorial(n))
