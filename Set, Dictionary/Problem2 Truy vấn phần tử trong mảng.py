if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    x = int(input())
    for i in range(x):
        t = int(input())
        if t in b:
            print("YES")
        else:
            print("NO")
    
