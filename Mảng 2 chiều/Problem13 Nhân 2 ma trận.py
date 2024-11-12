if __name__ == '__main__':
    n, m, p = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        t = list(map(int, input().split()))
        a.append(t)
    for _ in range(m):
        v = list(map(int, input().split()))
        b.append(v)
    c = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]
    for i in range(n):
        for j in range(p):
            print(c[i][j], end=' ')
        print()
