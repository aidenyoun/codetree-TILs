n = int(input())
a = list(map(int, input().split()))
temp = []

for i in range(0, len(a)-2):
    for j in range(i+2, len(a)):
        temp.append(a[i]+a[j])

print(max(temp))