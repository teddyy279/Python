if __name__ == '__main__':
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 1
    h1, h2, c1, c2 = 0, n - 1, 0, n - 1
    while cnt <= n * n:
        for i in range(c1, c2 + 1):
            a[h1][i] = cnt
            cnt += 1
        h1 += 1
        for i in range(h1, h2 + 1):
            a[i][c2] = cnt
            cnt += 1
        c2 -= 1
        for i in range(c2, c1 - 1, -1):  # Thêm bước lùi -1
            a[h2][i] = cnt
            cnt += 1
        h2 -= 1    
        for i in range(h2, h1 - 1, -1):  # Thêm bước lùi -1
            a[i][c1] = cnt
            cnt += 1
        c1 += 1  # Sửa lại từ c1 -= 1 thành c1 += 1
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
