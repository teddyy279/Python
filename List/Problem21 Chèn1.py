if _name_ == '_main_':
  n, x, k = map(int, input().split())
  a = list(map(int, input().split()))
  a.insert(k - 1, x)
  for i in range(len(a)):
    print(a[i], end = ' ')
