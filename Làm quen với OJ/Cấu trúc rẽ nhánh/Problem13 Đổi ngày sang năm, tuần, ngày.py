x = int(input())
if(x >= 365):
    print(x // 365, x // 7, x, sep = ' ')
elif(x >= 7):
    print(x // 7, x, sep = ' ')
else:
    print(x)