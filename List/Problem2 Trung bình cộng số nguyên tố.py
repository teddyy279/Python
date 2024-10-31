from math import *

def prime(n):
  if n < 2: return False
  for i in range(2, isqrt(n) + 1):
    if n % i == 0: return False
  return True
    
    
if _name_ == '_main_':
  n = int(input())
  a = list(map(int, input().split()))
  sum1 = 0
  cnt = 0
  for i in range(n):
    if(prime(a[i])):
      sum1 += a[i]
      cnt += 1
  print('%.3f' %(sum1 / cnt))
