class Status:
    def __init__(self, hight, weight, number):
        self.hight = int(hight)
        self.weight = int(weight)
        self.number = int(number)

n = int(input())
tmp1 = 1
ans = []
for i in range(n):
    tmp = list(map(int, input().split()))
    ans.append(Status(tmp[0], tmp[1], tmp1))
    tmp1 += 1

ans.sort(key=lambda x:(-x.hight, -x.weight, x.number))

for i in range(n):
    print(f"{ans[i].hight} {ans[i].weight} {ans[i].number}")