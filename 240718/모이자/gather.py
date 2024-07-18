n = int(input())
p = list(map(int, input().split()))
temp_list = []
temp = 0

for i in range(len(p)):
    for k in range(len(p)):
        temp += p[k]*abs(k-i)
    temp_list.append(temp)
    temp = 0

print(min(temp_list))