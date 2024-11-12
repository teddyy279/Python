# Initialize Fibonacci array large enough for any reasonable n
F = [0] * 100

def init():
    F[0], F[1] = 0, 1
    for i in range(2, 93):
        F[i] = F[i - 1] + F[i - 2]

if __name__ == '__main__':
    init()  
    n = int(input())
    
    # Create an n x n matrix
    a = [[0 for _ in range(n)] for _ in range(n)]
    
    # Define boundaries
    h1, h2 = 0, n - 1
    c1, c2 = 0, n - 1
    cnt = 0
    
    # Fill matrix in spiral order
    while cnt < n * n:
        for i in range(c1, c2 + 1):  
            a[h1][i] = F[cnt]
            cnt += 1
        h1 += 1
        
        for i in range(h1, h2 + 1):
            a[i][c2] = F[cnt]
            cnt += 1
        c2 -= 1
        
        for i in range(c2, c1 - 1, -1):  
            a[h2][i] = F[cnt]
            cnt += 1
        h2 -= 1
        
        for i in range(h2, h1 - 1, -1):  
            a[i][c1] = F[cnt]
            cnt += 1
        c1 += 1
    
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
