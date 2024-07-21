tmp = list(input())

ans = 0

for i in range(len(tmp)):
    if tmp[i] == "(":
        for k in range(i+1, len(tmp)):
            if tmp[k] == ")":
                ans += 1

print(ans)