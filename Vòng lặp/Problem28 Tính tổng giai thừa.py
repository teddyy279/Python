n = int(input())

res = 1
tmp = 1
for i in range(2, n + 1):
    tmp *= i
    res += tmp
print(res)
