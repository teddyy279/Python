c = input()
if(c == 'z' or c == 'Z'):
    print('a')
else:
    tmp = ord(c) #ord biến chữ cái thành số trong bảng mã ASCII
    tmp += 1
    print(chr(tmp).lower()) # chr biến vị trí trong bảng mã ASCII thành kí tự hoặc chữ 
    