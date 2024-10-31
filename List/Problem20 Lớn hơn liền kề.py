if _name_ == '_main_':
  n = int(input())
  a = list(map(int, input().split()))
  max1, max2 = 0, 0
  for x in a:
    if(x > max1):
      max2 = max1
      max1 = x
  print(max1, max2, sep = ' ')
