if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    count = 0
    i, j = 0, 0
    while(i < n and j < m):
        if(a[i] > b[j]):
            count += 1
            i += 1
            j += 1
        else:
            i += 1
    print(count)
