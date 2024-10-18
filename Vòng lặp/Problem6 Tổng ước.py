from math import*

n = int(input())

res = 1
for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        if i != n // i:
            res += i + n // i
        else:
            res += i
res += n  
print(res)
