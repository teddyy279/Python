def palindrome_number(n):
    tmp = n
    rev = 0
    while n != 0:
        rev *= 10
        rev += n % 10
        n //= 10
    return rev == tmp


if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b =  list(map(int, input().split()))
        a.append(b)
    cnt = 0
    for i in range(n):
        for j in range(i + 1):
            if(palindrome_number(a[i][j])):
                cnt += 1
    print(cnt)

