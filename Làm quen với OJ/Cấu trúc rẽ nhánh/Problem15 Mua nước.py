n, a, b = map(int, input().split())
if(b / 2 >= a): # b / 2 là tính nước trên 1 l của b 
    print(a * n)
else:
    if(n % 2 == 0):
        print(n // 2 * b)
    else: print((n - 1) // 2 * b + a)