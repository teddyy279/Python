a, b, c = map(int, input().split())
if (c * c) == (a * a + b * b):
    print("3")
elif a == b and b == c:
    print("1")
else: print("2")