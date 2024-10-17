m, n = map(int, input().split())
if(m % 2 == 0):
    print(m // 2 * n)
else:
    print(((m - 1) // 2) * n + n // 2)
