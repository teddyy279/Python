c1, c2, c3, c4, c5 = map(int, input().split())
if (c1 + c2 + c3 + c4 + c5) % 5 == 0:
    b = (c1 + c2 + c3 + c4 + c5) // 5
    if b != 0:
        print(b)
    else:
        print(-1)
else:
    print(-1)