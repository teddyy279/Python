if _name_ == '_main_':
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  sum1 = 0
  for i in range(k):
    sum1 += a[i]
  print(sum1 , end = ' ')
  for i in range(1,  n - k + 1):
    sum1 = sum1 - a[i - 1] + a[i + k - 1]
    print(sum1, end = ' ')
