if __name__ == '__main__':
    s = input()
    s += s[-1]
    max_len = 0
    max_substr = ""
    current_len = 1
    current_substr = s[0]

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            current_len += 1
            current_substr += s[i]
        else:
            if current_len > max_len:
                max_len = current_len
                max_substr = current_substr
            elif current_len == max_len:
                if current_substr > max_substr:
                    max_substr = current_substr
            current_substr = s[i]
            current_len = 1
        
    print(max_substr)
