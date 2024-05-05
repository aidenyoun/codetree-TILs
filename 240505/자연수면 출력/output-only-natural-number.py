a, b = map(int, input().split())
c = ""
if a > 0:
    for _ in range(b):
        c += str(a)
    print(c)
else:
    print("0")