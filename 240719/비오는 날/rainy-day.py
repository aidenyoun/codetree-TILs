n = int(input())
tmp = []
for i in range(n):
    tmp.append(input().split())
tmp.sort()
for i in range(n):
    if tmp[i][2] == "Rain":
        print(*tmp[i])
        break