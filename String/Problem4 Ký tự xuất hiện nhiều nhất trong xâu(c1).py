def find_max_min_characters(s):
    cnt = [0] * 256  # Khởi tạo mảng đếm với 256 phần tử bằng 0
    for char in s:
        cnt[ord(char)] += 1
    
    max_char, min_char = '', ''
    max_count, min_count = 0, float('inf')
    
    for i in range(256):
        if cnt[i] > max_count or (cnt[i] == max_count and chr(i) > max_char):
            max_char = chr(i)
            max_count = cnt[i]
        if cnt[i] > 0 and (cnt[i] < min_count or (cnt[i] == min_count and chr(i) > min_char)):
            min_char = chr(i)
            min_count = cnt[i]
    
    return max_char, max_count, min_char, min_count

max_char, max_count, min_char, min_count = find_max_min_characters(s)

print(max_char, max_count)
print(min_char, min_count)
