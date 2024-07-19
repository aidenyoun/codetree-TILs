class Region:
    def __init__(self, name, code, region):
        self.name = name
        self.code = code
        self.region = region

n = int(input())
ans = []
for _ in range(n):
    tmp = input().split()
    ans.append(Region(tmp[0], tmp[1], tmp[2]))

ans.sort(key=lambda x:x.name)
print(f"name {ans[n-1].name}")
print(f"addr {ans[n-1].code}")
print(f"city {ans[n-1].region}")