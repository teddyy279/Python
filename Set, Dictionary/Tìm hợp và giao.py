from collections import Counter

if __name__ == '__main__':
    n = int(input())
    a = set(list(map(int, input().split())))
    b = set(list(map(int, input().split())))
    c = list(a.intersection(b))
    d = list(a.union(b))
    c.sort()
    d.sort()
    for x in c:
        print(x, end = ' ')
    for x in d:
        print(x, end = ' ')
