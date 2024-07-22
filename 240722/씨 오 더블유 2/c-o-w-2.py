n = int(input())
a = list(input())
ans = 0
for i in range(len(a) - 2):
    for j in range(i+1, len(a) - 1):
        for k in range(j+1, len(a)):
            if a[i] == 'C' and a[j] == 'O' and a[k] == 'W':
                ans += 1
print(ans)