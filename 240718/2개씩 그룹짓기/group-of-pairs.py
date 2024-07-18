n = int(input())
l = list(map(int, input().split()))
l.sort()
max_sum = 0
for i in range(n):
    max_sum = max(max_sum, l[i] + l[2 * n - 1 - i])

print(max_sum)