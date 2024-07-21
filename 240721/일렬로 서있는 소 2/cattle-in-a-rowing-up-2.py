n = int(input())
temp = list(map(int, input().split()))
ans = 0

for i in range(len(temp)):
    for j in range(i+1, len(temp)):
        for k in range(j+1, len(temp)):
            if temp[i] <= temp[j] <= temp[k]:
                ans += 1

print(ans)