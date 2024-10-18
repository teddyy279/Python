a, b, c, n = map(int, input().split())
if (a + b + c + n) %  3 == 0:
  tmp = (a + b + c + n) // 3
  if(tmp >= a and  tmp >= b and tmp >= c): # kiểm tra số tiền chia đi cho 3 có lớn hơn cả 3 thằng hay không vì nếu có thằng không lớn hơn thì tức là tiền của thằng này đã san ra cho thằng kia rồi
    print("YES")
  else:
    print("NO")
else: print("NO")