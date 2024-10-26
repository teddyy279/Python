def fibo(n):
    fn1 = fn2 = 1
    res = 0
    for i in range(2, n):
        fn = fn1 + fn2
        print(fn)
        fn1, fn2 = fn, fn1

if __name__ == '__main__':
    n = int(input())
    if(n == 1):
        print(1)
    if(n >= 2):
        print(1)
        print(1)
    fibo(n) 
