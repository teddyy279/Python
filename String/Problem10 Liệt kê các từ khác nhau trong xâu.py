if __name__ == '__main__':
    s = input()
    a = s.split()
    se = set(a)
    for x in sorted(se):
        print(x, end = ' ')
    print()
    for x in se:
        print(x, end = ' ')
