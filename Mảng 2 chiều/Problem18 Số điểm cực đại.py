a = []
path = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def check(i, j):
    for x in path:
        i1 = i + x[0]
        j1 = j + x[1]
        if i1 <= n - 1 and j1 <= m - 1 and i1 >= 0 and j1 >= 0:
            if a[i][j] <= a[i1][j1]:
                return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if check(i, j):
                cnt += 1
    print(cnt)
