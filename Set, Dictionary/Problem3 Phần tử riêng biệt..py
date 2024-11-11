if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    s = set({})
    for i in range(len(a)):
        if a[i] not in s:
            print(a[i], end = ' ')
            s.add(a[i])
        
