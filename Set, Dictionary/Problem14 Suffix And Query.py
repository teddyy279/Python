if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    F = [0] * n
    s = set({})
    for i in range(n - 1, - 1, -1):
        s.add(a[i])
        F[i] = len(s)
    for _ in range(q):
        l = int(input())
        print(F[l])


"""
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l = int(input())
        s = set(a[l:])
        print(len(s))
"""    
