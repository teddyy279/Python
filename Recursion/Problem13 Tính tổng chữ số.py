def sum_digit(n):
    if n == 0:
        return 0
    if n != 0:
        return n % 10 + sum_digit(n // 10)

if __name__ == '__main__':
    n = int(input())
    print(sum_digit(n))
