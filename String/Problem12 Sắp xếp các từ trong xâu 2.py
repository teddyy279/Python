def check(s):
    t = s[::-1]
    return s == t

if __name__ == '__main__':
    s = input()
    a = s.split()
    se = set({})
    b = []
    for x in a:
        if check(x) and x not in se:
            b.append(x)
            se.add(x)
    b.sort(key = lambda x : len(x))
    for x in b:
        print(x, end = ' ')
