n = int(input())
l = list(map(int, input().split()))
ans = []
temp = 0
temp1 = 0
for i in range(len(l)):
    if i == 0:
        ans.append(l[i])
        temp += l[i]
        temp1 += 1
    elif i % 2 == 0:
        temp += l[i]
        temp1 += 1
        ans.append(temp//temp1)
print(*ans)