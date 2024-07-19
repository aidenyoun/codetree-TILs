class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)

n = int(input())
ans = []
for i in range(n):
    tmp = input().split()
    ans.append(Score(tmp[0], tmp[1], tmp[2], tmp[3]))

ans.sort(key=lambda x:(-x.kor, -x.eng, -x.math))

for i in range(n):
    print(f"{ans[i].name} {ans[i].kor} {ans[i].eng} {ans[i].math}")