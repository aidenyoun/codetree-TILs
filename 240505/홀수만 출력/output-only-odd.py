a, b = map(int, input().split())
d = []
for i in range(a, b+1, 2):
    d.append(i)
print(*d)