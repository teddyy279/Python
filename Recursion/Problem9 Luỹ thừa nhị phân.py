def binpow(a, b):
    if(b == 0): return 1
    X = binpow(a, b // 2)
    if(b % 2 == 0):
        return X * X 
    else: return X * X * a

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(binpow(a, b))
