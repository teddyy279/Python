if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    scare = 0
    a.sort()
    for i in range(len(a)):
        if(scare < a[i]):
            res += a[i] - scare
            scare += 1
    print(res)
