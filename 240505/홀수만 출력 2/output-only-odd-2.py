b, a = map(int, input().split())
c = []
for i in range(a, b+1, 2):
    c.append(i)

c.reverse()
print(*c)