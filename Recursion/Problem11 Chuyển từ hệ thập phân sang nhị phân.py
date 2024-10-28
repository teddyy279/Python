def F(n):
    if(n != 0):
        F(n // 2)
        print(n % 2, end = '')

if __name__ == '__main__':
    n = int(input())
    F(n)
