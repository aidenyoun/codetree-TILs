class Status:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)

n = int(input())
ans = []
for i in range(n):
    temp = input().split()
    ans.append(Status(temp[0], int(temp[1]), int(temp[2])))

ans.sort(key=lambda x:(x.height, -x.weight))
for i in range(n):
    print(f"{ans[i].name} {ans[i].height} {ans[i].weight}")