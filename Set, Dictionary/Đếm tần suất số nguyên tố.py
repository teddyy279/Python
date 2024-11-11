from math import*

def prime(n):
    if n < 2: return False
    for i in range(2, sqrt(n)):
        if(n % i == 0):
            return False
    return True

if __name__ == '__main__':
    a = list(map(int, input().split()))
    d = dict({})
    for i in range(len(a)):
        if prime(a[i]):
            if a[i] in d:
                d[a[i]] += 1
            else:
                d[a[i]] = 1
    for key, value in d.items:
        print(key, value)
