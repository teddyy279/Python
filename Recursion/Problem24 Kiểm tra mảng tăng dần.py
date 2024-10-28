def check(a, right):
    if(right == 0): return True
    else:
        if(a[right - 1] > a[right]):
            return check(a, right - 1)
        else: return False

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if(check(a, n - 1)): print("YES")
    else: print("NO")
