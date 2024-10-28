def F(n):
    if(n == 1): return 0
    if(n % 3 == 0):
        return 1 + F(n // 3)
    if(n % 2 == 0):
        return 1 + F(n // 2)
    return 1 + F(n - 1)

if __name__ == '__main__':
    n = int(input())
    print(F(n))
