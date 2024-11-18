if __name__ == '__main__':
    s = input()
    t = input()
    a = set(s.lower().split())
    b = set(t.lower().split())
    for x in sorted(a):
        if x in b:
            print(x, end = ' ')
