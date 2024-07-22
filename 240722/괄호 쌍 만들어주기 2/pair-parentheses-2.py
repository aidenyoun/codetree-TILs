a = list(input())

ans = 0

for i in range(len(a)):
    for j in range(i+2, len(a)-1):
        if a[i] == '(' and a[i+1] == '(' and a[j] == ')' and a[j+1] == ')':
            ans += 1

print(ans)