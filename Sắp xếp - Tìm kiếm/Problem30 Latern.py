if __name__ == '__main__':
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    max_distance = -1
    for i in range(1, len(a)):
        if (a[i] - a[i - 1]) > max_distance:
            max_distance = a[i] - a[i - 1]
    print('%.10f' %(max_distance / 2))
