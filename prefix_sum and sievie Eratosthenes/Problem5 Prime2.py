from math import*

prime = [0] * (10 ** 6 + 1)

def sieve():
  for i in range(0, 10 ** 6 + 1):
    prime[i] = 1
  prime[0] = prime[1] = 0
  for i in range(2, isqrt(10 ** 6 + 1)):
    if(prime[i]):
      for j in range(i * i, 10 ** 6 + 1, i):
        prime[j] = 0 
    

F = [0] * (10 ** 6 + 1)
def init():
  F[0] = prime[0]
  for i in range(1, 10 ** 6 + 1):
    F[i] = F[i - 1] + prime[i]

if __name__ == '__main__':
  sieve()
  init()
  t = int(input())
  for i in range(t):
    left, right = map(int, input().split())
    print(F[right] - F[left - 1])
  
