n = int(input())
b = []
for _ in range(n):
    a = int(input())
    if a % 3 == 0:
        b.append(a)

for i in b:
    print(i)