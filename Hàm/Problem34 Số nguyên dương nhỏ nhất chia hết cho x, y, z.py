from math import*

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b //  gcd(a, b)

if __name__ == '__main__':
    x, y, z, n = map(int, input().split())
    bc = lcm(lcm(x, y), z)
    tmp = 10 ** (n - 1) # số nhỏ nhất có n chữ số
    ans = (tmp + bc - 1) // bc * bc # số nhỏ nhất lớn hơn số có n chữ số mà chia hết cho bội chung
    if ans < 10 ** n:
        print(ans)
    else: print(-1)
