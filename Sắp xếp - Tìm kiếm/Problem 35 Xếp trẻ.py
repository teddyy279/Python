def solve(a, pos, x, cnt):
    if pos == len(a):
        return cnt
    if a[pos] + a[pos - 1] < x:
        cnt = solve(a, pos + 1, x, cnt)
    else:
        cnt += 1
        cnt = solve(a, pos + 1, x, cnt)
    return cnt

if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(solve(a, 1, x, 1))
