if __name__ == '__main__':
    n, power_of_kirito = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    a.sort(key = lambda x : x[0])
    check = 1
    for x, y in a:
        if power_of_kirito > x:
            power_of_kirito += y
        else:
            check = 0 
    if(check): 
        print("YES")
    else:
        print("NO")
