if __name__ == '__main__':
    s = input()
    d = dict({})
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    for char in sorted(d):
        print(char, d[char], end = '\n')
    print()
    for x in d:
        print(x, d[x], end = '\n')

