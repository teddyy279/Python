    if __name__ == '__main__':
        n = int(input())
        a = list(map(int, input().split()))
        l, r = min(a), max(a)
        cnt = [0] * (10 ** 6 + 1)
        for x in a:
            cnt[x] = 1
        ans = 0
        for i in range(l, r + 1):
            if cnt[i] == 0: ans += 1
        print(ans)
    
