if _name_ == '_main_':
  n, x = map(int, input().split())
  a = list(map(int, input().split()))
  if x in a:
    a.remove(x)
    for i in range(len(a)):
      print(a[i], end = ' ')
  else:
    print("NOT FOUND")
    
