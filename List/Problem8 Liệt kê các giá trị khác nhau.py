if _name_ == '_main_':
  n = int(input())
  a = list(map(int, input().split()))
  d = [0] * 10000001
  for i in range(len(a)):
    if(d[a[i]] == 0):
      print(a[i], end = ' ')
      d[a[i]] += 1
