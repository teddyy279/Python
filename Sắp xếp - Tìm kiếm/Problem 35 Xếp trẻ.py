def min_gondolas(n, x, weights):
    weights.sort()
    i, j = 0, n - 1
    gondolas = 0

    while i <= j:
        if weights[i] + weights[j] <= x:
            i += 1
        j -= 1
        gondolas += 1

    return gondolas

if __name__ == '__main__':
    n, x = map(int, input().split())
    weights = list(map(int, input().split()))
    print(min_gondolas(n, x, weights))
