from math import *

prime = [0] * (10 ** 6 + 1)

def sieve():
  for i in range(0 , 10 ** 6 + 1):
    prime[i] = 1
  prime[0] = prime[1] = 0
  for i in range(2, isqrt(10 ** 6 + 1) + 1):
    if(prime[i] == 1):
      for j in range(i * i, 10 ** 6 + 1, i):
        prime[j] = 0

if __name__ == '__main__':
  sieve()
  t = int(input())
  for i in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, n + 1):
      if(prime[i]): cnt += 1
    print(cnt)
