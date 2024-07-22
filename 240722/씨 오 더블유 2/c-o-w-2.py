n = int(input())
a = list(input())
ans = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(i+2, len(a)):
            if a[i] == 'C' and a[j] == 'O' and a[k] == 'W':
                ans += 1
print(ans)