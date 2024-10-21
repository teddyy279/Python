n = int(input())

while(n >= 10):
    res = 0
    while n:
        res += n % 10
        n //= 10
    n = res
print(n)
