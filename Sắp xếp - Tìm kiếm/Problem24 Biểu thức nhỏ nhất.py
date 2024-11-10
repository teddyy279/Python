def solve(a, n, x):
    res = 0
    tmp1 = x
    for i in range(len(a)):
        if(tmp1 >= 1):
            res -= a[i]
            tmp1 -= 1
        else:
            res += a[i]
    return res
    
if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(solve(a,n, x))
    
