def check(n):
    fn1, fn2 = 1, 1
    tmp = n
    for i in range(3, 100):
        fn = fn1 + fn2
        if(tmp == fn): return True
        fn1, fn2 = fn, fn1
    return False

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if(n == 1 or n == 2): 
            print("YES")
        else:
            if(check(n)): print("YES")
            else: print("NO")
