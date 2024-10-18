n = int(input())
for i in range(1, n + 1):
  print(i, end = ' ')
print("\n")
for i in range(n, -1, -1):
  print(i, end = ' ')
print("\n")
for i in range(0, n, 2):
  print(i, end = ' ')
for i in range(1, n + 1, 2):
  print(i, end = ' ')
print("\n")
for i in range(5):
  if(i % 4 == 0):
    print(i , end = ' ')
print("\n")
for i in range(97, 97 + n):
  print(chr(i) , end = ' ')
print("\n")
for i in range(122 - n + 1, 122 + 1):
  print(chr(i), end = ' ')
