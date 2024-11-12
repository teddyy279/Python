if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    
    F = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                F[i][j] = a[i][j]
            elif i == 0:
                F[i][j] = F[i][j - 1] + a[i][j]
            elif j == 0:
                F[i][j] = F[i - 1][j] + a[i][j]
            else:
                F[i][j] = max(F[i - 1][j] + a[i][j], F[i][j - 1] + a[i][j])
    
    print(F[n-1][m-1])
