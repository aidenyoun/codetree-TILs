a = 0
cnt = 0
while True:
    i = int(input())
    if i < 20 or i > 29:
        break
    else:
        a += i
        cnt += 1

print(f"{a/cnt:.2f}")