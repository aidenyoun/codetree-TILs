n = int(input())
l = list(map(int, input().split()))
l.sort()
print(*l)
l.sort(reverse=True)
print(*l)