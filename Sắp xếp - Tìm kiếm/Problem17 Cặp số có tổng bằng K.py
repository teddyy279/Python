def Binary_Search1(a, l, r, x):
    left, right = l , r - 1
    res = -1
    while(left <= right):
        mid = (left + right) // 2
        if(a[mid] == x):
            res = mid 
            right = mid - 1
        elif(a[mid] > x):
            right = mid - 1
        else:
            left = mid + 1
    return res

def Binary_Search2(a, l, r, x):
    left, right = l, r - 1
    res = -1
    while(left <= right):
        mid = (left + right) // 2
        if(a[mid] == x):
            res = mid
            left = mid + 1
        elif(a[mid] > x):
            right = mid - 1
        else:
            left = mid + 1
    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(len(a)):
        if (Binary_Search1(a, i + 1, n, k - a[i]) != -1):
          cnt += Binary_Search2(a, i + 1, n, k - a[i]) - Binary_Search1(a, i + 1, n, k - a[i]) + 1
    print(cnt)  
