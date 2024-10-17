from math import*

n = float(input())
if (n - int(n)) >= 0.5:
    print(ceil(n))
else:
    print(int(n))