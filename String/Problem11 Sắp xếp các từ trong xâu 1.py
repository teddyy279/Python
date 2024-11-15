if __name__ == '__main__':
    s = input()
    a = s.split()
    for x in sorted(a):
        print(x, end = ' ')
    print()
    a.sort(key = lambda x : (len(x), x))
    print(' '.join(a))
