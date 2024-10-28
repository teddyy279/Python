def sum1(n):
    if n == 1: return 1
    return 1 / n + sum1(n - 1)

if __name__ == '__main__':
    n = int(input())
    print('%.3f' %sum1(n))
