if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    for i in b:
        print(i , end = ' ')
