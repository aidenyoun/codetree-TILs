class People:
    def __init__(self, name, hight, weight):
        self.name = name
        self.hight = hight
        self.weight = weight

n = int(input())
ans = []
for i in range(n):
    tmp = input().split()
    ans.append(People(tmp[0], tmp[1], tmp[2]))

ans.sort(key=lambda x:x.hight)

for i in range(n):
    print(f"{ans[i].name} {ans[i].hight} {ans[i].weight}")