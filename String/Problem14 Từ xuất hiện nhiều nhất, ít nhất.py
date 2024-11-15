if __name__ == '__main__':
    s = input()
    a = s.split()
    d = dict({})
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    min_fre, max_fre = 10 ** 18, 0
    res1, res2 = ' ', ' '
    for x in sorted(d):
        if d[x] <= min_fre:
            res1 = x
            min_fre = d[x]
        if d[x] >= max_fre:
            res2 = x
            max_fre = d[x]
    print(max_fre, res2)
    print(min_fre, res1)
