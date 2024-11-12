if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
            b = list(map(int, input().split()))
            a.append(b)
    for i in range(n):
        sum_rows = 0 
        for j in range(m):
            sum_rows += a[i][j]
        print(sum_rows, end = ' ')
    print()
    for i in range(n):
        sum_columns = 0
        for j in range(m):
            sum_columns += a[j][i]
        print(sum_columns, end = ' ')
    
