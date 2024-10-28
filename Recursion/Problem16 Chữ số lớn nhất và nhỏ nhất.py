from math import*

def find_max(n):
    if(n < 10):
        return n
    else:
        return max(n % 10, find_max(n // 10))

def find_min(n):
    if(n < 10):
        return n
    else: return min(n % 10, find_min(n // 10))

if __name__ == '__main__':
    n = int(input())
    print(find_max(n), end = ' ')
    print(find_min(n))
