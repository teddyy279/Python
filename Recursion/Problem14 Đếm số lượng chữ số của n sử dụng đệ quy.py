def cnt_digit(n):
    if n == 0: return 0
    if n != 0:
        return 1 + cnt_digit(n // 10)

if __name__ == '__main__':
    n = int(input())
    print(cnt_digit(n))
