n = int(input())

res, tmp = 0, 0
while n:
  if(n >= 28):
    n -= 28
    res += 1
    tmp += 1
  else: break;
  if(tmp >= 3):
    res += 1
    tmp = 1
print(res)
