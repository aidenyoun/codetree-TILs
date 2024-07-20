class Line:
    def __init__(self, height, weight, number):
        self.height = int(height)
        self.weight = int(weight)
        self.number = int(number)
n = int(input())

ans = []
number = 1
for i in range(n):
    temp = list(map(int, input().split()))
    ans.append(Line(temp[0], temp[1], number))
    number += 1

ans.sort(key=lambda x:(x.height, -x.weight))

for i in range(n):
    print(f"{ans[i].height} {ans[i].weight} {ans[i].number}")