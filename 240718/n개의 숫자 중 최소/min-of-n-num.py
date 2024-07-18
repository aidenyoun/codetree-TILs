a = int(input())
b = list(map(int, input().split()))

print(f"{min(b)} {b.count(min(b))}")