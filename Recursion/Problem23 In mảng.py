def print1(a, left, n):
    if left == n:
        return
    print(a[left], end=' ')
    print1(a, left + 1, n)

def print2(a, right):
    if right == 0:
        return
    print(a[right - 1], end=' ')
    print2(a, right - 1) 

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print1(a, 0, n)  
    print()  
    print2(a, n)  
