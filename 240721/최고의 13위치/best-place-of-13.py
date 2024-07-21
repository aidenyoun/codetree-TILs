n = int(input())
temp = []
temp1 = 0
max_temp = 0
ans = 0
for i in range(n):
    temp.append(list(map(int, input().split())))

if len(temp) == 3:
    for i in range(len(temp)):
        temp1 = temp[i].count(1)
        max_temp = max(temp1, max_temp)
        ans = max_temp

else:
    for i in range(len(temp)):
        for j in range(len(temp)-2):
            if temp[i][j] == 1:
                temp1 += 1
            if temp[i][j+1] == 1:
                temp1 += 1
            if temp[i][j+2] == 1:
                temp1 += 1
            max_temp = max(temp1, max_temp)
            ans = max_temp
            temp1 = 0

print(ans)