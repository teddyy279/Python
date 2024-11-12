if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
            b = list(map(int, input().split()))
            a.append(b)
    min_val, max_val = 10 ** 18 + 1, 0
    for row in a:
        min_val = min(min_val, min(row))
        max_val = max(max_val, max(row))
    print(min_val)
    for i in range(n):
        for j in range(m):
            if a[i][j] == min_val:
                print(i + 1, j + 1, end = ' ')
                print()
    print(max_val)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_val:
                print(i + 1, j + 1, end = ' ')
                print()
