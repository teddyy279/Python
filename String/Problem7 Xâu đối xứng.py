def check(s):
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    s1 = input()
    if check(s1):
        print("YES")
    else:
        print("NO")
