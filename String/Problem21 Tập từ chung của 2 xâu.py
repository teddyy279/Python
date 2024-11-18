if __name__ == '__main__':
    s = input()
    t = input()
    a = set(s.lower().split())
    b = set(t.lower().split()) # phải dùng lower() trước khi biến thành set tại set không thay đổi được các phần tử của nó 
    for x in sorted(a):
        if x in b:
            print(x, end = ' ')
