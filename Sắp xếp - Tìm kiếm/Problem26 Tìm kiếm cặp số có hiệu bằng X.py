def Binary_Search(a, left, right, x):
    l, r = left, right 
    while(l <= r):
        mid = (l + r) // 2
        if(a[mid] == x):
            return True
        elif(a[mid] > x):
            r = mid - 1
        else:
            l = mid + 1
    return False

if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    check = 0
    for i in range(1, len(a)):
        if(Binary_Search(a, i + 1, n - 1, x - a[i])):
            print(1)
            check = 1
            break
    if(check == 0): print(-1)
