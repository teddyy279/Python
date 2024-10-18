a1, a2, a3, b1, b2, b3 =  map(int, input().split())
n = int(input())
TotalCup = a1 + a2 + a3
TotalMedal = b1 + b2 + b3
if TotalCup % 5 == 0:
  res1 = TotalCup // 5
else:
  res1 = TotalCup // 5 + 1
if TotalMedal % 10 == 0:
  res2 = TotalMedal // 10
else:
  res2 = TotalMedal // 10 + 1
if(res1 + res2 <= n): print("YES")
else: print("NO")