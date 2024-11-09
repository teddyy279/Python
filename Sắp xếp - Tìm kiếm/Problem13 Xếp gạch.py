if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    cnt = 1
    tmp = a[0]
    for i in range(1, n):
        if(tmp > 0):
            cnt += 1
            tmp = min(tmp - 1, a[i])
    print(cnt)

