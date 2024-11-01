if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    fre_max = 1
    tmp = 1
    res = a[0]
    a.sort()
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            fre_max += 1
        else:
            if fre_max > tmp:
                tmp = fre_max
                res = a[i - 1]
            fre_max = 1
    if fre_max > tmp:
        tmp = fre_max
        res = a[-1]
    print(res, tmp, sep=' ')
