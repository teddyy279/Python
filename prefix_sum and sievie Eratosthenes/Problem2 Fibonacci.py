
F = [0] * 100 

def init():
  F[0] = 0
  F[1] = 1
  for i in range(2, 93):
    F[i] = F[i - 1] + F[i - 2]

if __name__ == '__main__':
  init()
  t = int(input())
  for i in range(t):
    n = int(input())
    print(F[n])
