def Fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

if _name_ == '_main_':
    n = int(input())
    print(Fibonacci(n))
