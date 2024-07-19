n = int(input())
l = list(map(int, input().split()))
temp = []
ans = []
for i in range(len(l)):
    temp.append(l[i])
    if i % 2 == 0:
        temp.sort()
        ans.append(temp[(i//2)])

print(*ans)