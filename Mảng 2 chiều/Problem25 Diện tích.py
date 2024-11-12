a = []
path = [[-1, 0], [0, - 1], [1, 0], [0, 1]]

def flood_fill(i, j, cnt):
    a[i][j] = 0
    for x, y in path:
        i1 = i + x
        j1 = j + y
        if i1 >= 0 and i1 <= n - 1 and j1 >= 0 and j1 <= m - 1 and a[i1][j1] == 1:
            return flood_fill(i1, j1, cnt + 1)
    return cnt

if __name__ == '__main__':
    n, m = map(int, input().split())
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    max_area = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                max_area = max(flood_fill(i, j, 1), max_area)
    print(max_area)
    
