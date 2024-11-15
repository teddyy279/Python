if __name__ == '__main__':
    s = input()
    a = s.split()
    d = dict({})
    for x in a:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    for x, y in sorted(d.items()):
        print(x, y, end = '\n')
    print()
    for x in d:
        print(x, d[x], end = '\n')
