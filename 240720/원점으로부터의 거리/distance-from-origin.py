class Dot:
    def __init__(self, xx, yy, count):
        self.xx = int(xx)
        self.yy = int(yy)
        self.count = int(count)

n = int(input())
temp1 = 1
ans = []
for i in range(n):
    temp = list(map(int, input().split()))
    ans.append(Dot(temp[0], temp[1], temp1))
    temp1 += 1

ans.sort(key=lambda x:(((abs(0 - x.xx) + abs(0 - x.yy)), x.count)))
for i in range(n):
    print(f"{ans[i].count}")