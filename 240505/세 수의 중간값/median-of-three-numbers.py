a, b, c = map(int, input().split())

if b > a:
    if b < c:
        print("1")
    else:
        print("0")
else:
    print("0")