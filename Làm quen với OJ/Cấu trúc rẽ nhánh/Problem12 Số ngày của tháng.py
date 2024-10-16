a, b = map(int, input().split())

if(a % 2 == 0 and b % 4 == 0 and  b % 100 != 0): print(29)
elif(a % 2 == 0): print(31)
if(a % 2 != 0): print(30)