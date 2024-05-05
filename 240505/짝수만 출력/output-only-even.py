a, b = map(int, input().split())
c = []
for i in range(a, b+1):
    if i % 2 == 0:
        c.append(i)

c.sort()
print(*c)