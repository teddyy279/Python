def is_beautiful_number(s):
    increasing = True
    decreasing = True
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            increasing = False
        if s[i] > s[i - 1]:
            decreasing = False
    return increasing or decreasing


if __name__ == '__main__':
    s = input()  
    if is_beautiful_number(s):
        print("YES")
    else:
        print("NO")
