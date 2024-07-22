n, s = map(int, input().split())
temp = list(map(int, input().split()))
ans = []

temp.sort()
for i in range(0, len(temp)-3):
    for j in range(i+1, len(temp)-2):
        for k in range(j+1, len(temp)-1):
            for l in range(k+1, len(temp)):
                ans.append(abs(s - (temp[i]+temp[j]+temp[k]+temp[l])))

print(min(ans))