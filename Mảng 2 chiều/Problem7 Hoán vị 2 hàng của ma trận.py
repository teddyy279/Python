if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    for i in range(n):
        a[u][i], a[v][i] = a[v][i], a[u][i]
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = ' ')
        print()
