l = list(input().split())
l0 = int(l[0])  # 7
l1 = int(l[1])  # 3
temp = []
for _ in range(l0):
    a = input()
    if l[2] in a:
        temp.append(a)
temp.sort()
print(temp[l1-1])