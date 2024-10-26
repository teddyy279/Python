def fibo(n):
    fn1, fn2 = 1, 1
    tmp = n
    for i in range(3, 100):
        fn = fn1 + fn2 
        fn1, fn2 = fn, fn1
        if(fn >= n): 
            print(fn)
            return True
    return False

if __name__ == '__main__':
    n = int(input())   
    if(n == 1): print(1)
    if(n == 2): print(1)
    else:
        fibo(n)
