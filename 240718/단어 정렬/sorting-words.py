n = int(input())
l = []
for _ in range(n):
    l.append(input())

l.sort()

for i in range(n):
    print(l[i])