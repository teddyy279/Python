from functools import cmp_to_key

def compare(a, b):
    ab = a + b
    ba = b + a
    if ab > ba:
        return -1
    else:
        return 1

if __name__ == '__main__':
    n = int(input())
    a = input().split()
    a.sort(key = cmp_to_key(compare))
    print(''.join(a))
