def Binary_Search1(a, n, x):
    left, right = 0, n - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            res = mid
            right = mid - 1
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return res

def Binary_Search2(a, n, x):
    left, right = 0, n - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            res = mid
            left = mid + 1
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return res

def Binary_Search3(a, n, x):
    left, right = 0, n - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] >= x:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

def Binary_Search4(a, n, x):
    left, right = 0, n - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > x:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(Binary_Search1(a, n, k))
    print(Binary_Search2(a, n, k))
    print(Binary_Search3(a, n, k))
    print(Binary_Search4(a, n, k))
    if(Binary_Search1(a, n, k) != -1):
        print(Binary_Search2(a, n, k) - Binary_Search1(a, n, k) + 1)
    else:
        print(0)
