if __name__ == '__main__':
    s = input()
    s += '#'
    max_len = 0
    max_char = ''
    current_len = 1
    current_char = s[0]

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_len += 1
            current_char = s[i]
        else:
            if current_len > max_len or (current_len == max_len and current_char > max_char):
                max_len = current_len
                max_char = current_char
            current_len = 1
            current_char = s[0]
    for i in range(max_len):
        print(max_char, end = '')
