if __name__ == '__main__':
    n = int(input())
    a = []
    d = dict({})
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    for i in range(n):
        for j in range(n):
            if a[i][j] not in d:
                d[a[i][j]] = 1
            else:
                if d[a[i][j]] == i:
                    d[a[i][j]] = i + 1
    d = list(d.items())
    d.sort(key = lambda x : x[0])
    for x, y in d:
        if y == n:
            print(x, end = ' ')

