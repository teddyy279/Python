def check(n):
    if(n == 0 and n == 1): return True
    fn1, fn2 = 1, 0
    for i in range(2, 100):
        fn = fn1 + fn2 
        if(fn == n):
            return True
        fn1, fn2 = fn, fn1
    return False

if __name__ == '__main__':
    n = int(input())   
    if(check(n)): print("YES")
    else: print("NO")
