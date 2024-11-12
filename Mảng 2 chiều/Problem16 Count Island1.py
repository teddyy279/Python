path = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def loang(a, i , j):
    a[i][j] = 0
    for x in path:
        i1 = i + x[0]
        j1 = j + x[1]
        if(i1 <= n - 1 and i1 >= 0 and j1 <= m - 1 and j1 >= 0 and a[i1][j1] == 1):
            loang(a, i1, j1)

if __name__ == '__main__':
    n, m = map(int,input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if(a[i][j] == 1):
                cnt += 1
                loang(a, i, j)
    print(cnt)            
