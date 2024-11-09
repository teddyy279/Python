if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 1
    a.sort()
    for i in range(1, len(a)):
        if(a[i] - a[i - 1] > k):
            cnt += 1
    print(cnt)
