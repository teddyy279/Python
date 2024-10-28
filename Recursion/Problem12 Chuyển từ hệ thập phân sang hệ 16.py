def F(n):
    if(n != 0):
        F(n // 16)
        r = n % 16
        if(r <= 9):
            print(r, end = '')
        else: 
            print(chr(r + 55), end = '') # chr in ra kí tự trong mã ascii A =65(kí tự đầu tiên tương ứng 10 trong hệ 16) nên cộng với 55 là đủ 

if __name__ == '__main__':
    n = int(input())
    F(n)
