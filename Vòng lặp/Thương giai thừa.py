from math import*

n = int(input())

res = 0
for i in range(n):
    res += 1 / factorial(i)
print("%.4f" % res)
