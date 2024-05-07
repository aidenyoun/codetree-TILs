cnt = 2
n = int(input())
print("*"*(n*2))
while n >= 1:
    n -= 1
    print("*" * n + " " * cnt + "*" * n)
    cnt += 2