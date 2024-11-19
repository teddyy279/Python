if __name__ == '__main__':
    s = input()
    F = [1] * (len(s) + 1)
    max_len = 0
    for i in range(1, len(s)):
        if(s[i] == s[i - 1]):
            F[i] = max(F[i - 1] + 1, F[i])
            max_len = max(F[i], max_len)
    res = ''
    for i in range(len(s)):
        if F[i] == max_len and s[i] > res:
            res = s[i]
    print(res * max_len)
    
