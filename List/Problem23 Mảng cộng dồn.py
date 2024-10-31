if _name_ == '_main_':
  n = int(input())
  a = list(map(int, input().split()))
  F = [0] * (n + 1)
  F[0] = a[0]
  for i in range(1, len(a)):
    F[i] = F[i - 1] + a[i]
  for i in range(len(a)):
    print(F[i], end = ' ')
