def Recursion_Binary_Search(a, left, right, x):
    if(left > right): return False
    mid = (left + right) // 2
    if(a[mid] == x):
        return True
    elif(a[mid] > x):
        return Recursion_Binary_Search(a, left, mid - 1, x)
    else: return Recursion_Binary_Search(a, mid + 1, right, x)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    if(Recursion_Binary_Search(a, 0, n - 1, x)): print("YES")
    else: print("NO")
