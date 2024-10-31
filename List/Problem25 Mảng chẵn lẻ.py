from sys import stdin

if _name_ == '_main_':
  a = []
  for s in stdin:
    a += list(map(int, s.split()))
  even, odd = 0, 0
  for i in range(len(a)):
    if(a[i] % 2 == 0):
      even += 1
    else: odd += 1
  if(even > odd): print("CHAN")
  else: print("LE")
