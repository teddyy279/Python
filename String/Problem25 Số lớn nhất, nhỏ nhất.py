if __name__ == '__main__':
    m, s = map(int, input().split())
    ans_min, ans_max = [0] * m, [0] * m
    if s > 9 * m or (s == 0 and m > 1):
        print("NOT FOUND")
        exit()
    else:
        tmp = s
        for i in range(m):
            if s >= 9:
                ans_max[i] = 9
                s -= 9
            else:
                ans_max[i] = s
                s = 0
        if tmp // 9 < m:
            tmp -= 1
        for i in range(m - 1, 0, -1):
            if tmp >= 9:
                ans_min[i] = 9
                tmp -= 9
            else:
                ans_min[i] = tmp
                tmp = 0
        ans_min[0] = tmp + 1
        for i in range(m):
            print(ans_min[i], end = '')
        print()
        for i in range(m):
            print(ans_max[i], end = '')


