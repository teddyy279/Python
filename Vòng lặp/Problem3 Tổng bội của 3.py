n = int(input())
res = 0
for i in range(3, n + 1):
  if(i % 3 == 0): res += i
print(res)
