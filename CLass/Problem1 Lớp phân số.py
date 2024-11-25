def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class PhanSo:
    def __init__(self, tu, mau):
        self.__tu = tu
        self.__mau = mau

    def toi_gian(self):
        ucln = gcd(self.__tu, self.__mau)
        self.__tu //= ucln
        self.__mau //= ucln

    def __str__(self):
        return f'{self.__tu}/{self.__mau}'

if __name__ == '__main__':
    tu, mau = map(int, input().split())
    p = PhanSo(tu, mau)
    p.toi_gian()
    print(p)
