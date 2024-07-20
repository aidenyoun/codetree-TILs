class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)

ans = []
for i in range(5):
    tmp = input().split()
    ans.append(Info(tmp[0], int(tmp[1]), float(tmp[2])))
ans.sort(key=lambda x:x.name)
print("name")
for i in range(5):
    print(f"{ans[i].name} {ans[i].height} {ans[i].weight}")
print("")
ans.sort(key=lambda x:-x.height)
print("height")
for i in range(5):
    print(f"{ans[i].name} {ans[i].height} {ans[i].weight}")