def c(n, m):
    for _ in range (n):
        print("1" * m)
a, b = map(int, input().split())
c(a, b)