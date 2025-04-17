if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        d = dict({})
        a = list(map(int, input().split()))
        for i in range(len(a)):
            if a[i] in d:
                d[a[i]] += 1
            else:
                d[a[i]] = 1
        c = sorted(d.items(), key = lambda x : (-x[1], x[0]))
        for key, value in c:
            for _ in range(value):
                print(key, end = ' ')
        print()
