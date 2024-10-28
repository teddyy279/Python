def combination(n, k):
    if k == 0 or n == k: return 1
    else:
        return combination(n - 1, k - 1) + combination(n - 1, k)

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(combination(n, k)) 
