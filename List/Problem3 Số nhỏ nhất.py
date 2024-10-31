if _name_ == '_main_':
  n = int(input())
  a = list(map(int, input().split()))
  min_val = min(a)
  cnt = 0
  for i in range(len(a)):
    if(a[i] == min_val): cnt += 1
  print(cnt)
