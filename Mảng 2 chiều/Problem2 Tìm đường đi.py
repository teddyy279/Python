a = []
path = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def loang(i, j):
    a[i][j] = 0
    for x, y in path:
        i1 = i + x
        j1 = j + y
        if i1 <= n - 1 and  j1 >= m - 1 and i1 >= 0 and j1 >= 0 and a[i1][j1] == 1:
            loang(i1, j1)
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    u, v, s, t = map(int, input().split())
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    if a[u - 1][v - 1] == 1 and a[s - 1][t - 1] == 1:
        loang(u - 1, v - 1)
        if a[s - 1][t - 1] == 0:
            print("YES")
        else:
            print("NO")
    else: 
        print("NO")
    

