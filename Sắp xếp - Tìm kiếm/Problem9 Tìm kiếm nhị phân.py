def Binary_Search(a, n, x):
  left, right = 0, n - 1
  while(left <= right):
    mid = (left + right) // 2
    if(a[mid] == x): return True
    elif(x > a[mid]): right = mid - 1
    else: left = mid + 1
  return False
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    t = int(input())
    for i in range(t):
      x = int(input())
      if(Binary_Search(a, n, x)): print("YES")
      else: print("NO")
