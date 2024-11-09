def Binary_Search(a, left, right, x):
    l, r = left, right
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1
            res = mid
    return res

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    a.sort()
    for i in range(len(a)):
        pos = Binary_Search(a, i + 1, n - 1, k - a[i])
        if pos != -1:
            ans += (pos - i)
    print(ans)
