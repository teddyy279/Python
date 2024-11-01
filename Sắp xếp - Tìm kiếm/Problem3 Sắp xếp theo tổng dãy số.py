from functools import cmp_to_key

def sum_digit(n):
  res = 0
  while(n != 0):
    res += n % 10
    n //= 10
  return res
  
def cmp(a, b):
  sum1 = sum_digit(a)
  sum2 = sum_digit(b)
  if(sum1 != sum2):
    return sum1 - sum2
  else: return a - b

if __name__ == '__main__':
  n = int(input())
  a = list(map(int, input().split()))
  a.sort(key = cmp_to_key(cmp))
  for i in range(len(a)):
    print(a[i], end = ' ')
