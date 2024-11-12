a = []
knight_moves = [
    [-2, -1], [-2, 1], 
    [-1, -2], [-1, 2], 
    [1, -2], [1, 2], 
    [2, -1], [2, 1]
]

def flood_fill(i, j):
    a[i][j] = 0
    for x, y in knight_moves:
        i1 = i + x
        j1 = j + y
        if i1 <= n - 1 and j1 <= n - 1 and i1 >= 0 and j1 >= 0 and a[i1][j1] == 1:
            flood_fill(i1, j1)

if __name__ == '__main__':
    n = int(input())
    u, v, s, t = map(int, input().split())
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    flood_fill(u - 1, v - 1)
    if a[s - 1][t - 1] == 0:
        print("YES")
    else:
        print("NO")
