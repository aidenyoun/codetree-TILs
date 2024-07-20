a, b, c, d = map(int, input().split())

hours = c - a
minutes = d - b

print(hours*60 + minutes)