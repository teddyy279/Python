if __name__ == '__main__':
    s = input()
    d = dict({})
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    min_fre, max_fre = 10 ** 18, 0
    res1, res = ' ', ' '
    for char in sorted(d):
        if d[char] >= max_fre:
            max_fre = d[char]
            res1 = char
        elif d[char] <= min_fre:
            min_fre = d[char]
            res2 = char
    print(res1, max_fre, end = '\n')
    print(res2, min_fre, end = '\n')
