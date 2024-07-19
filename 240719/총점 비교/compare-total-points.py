class Student:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = int(score1)
        self.score2 = int(score2)
        self.score3 = int(score3)

n = int(input())
ans = []
for i in range(n):
    tmp = input().split()
    ans.append(Student(tmp[0], tmp[1], tmp[2], tmp[3]))

ans.sort(key=lambda x:x.score1 + x.score2 + x.score3)
for i in range(n):
    print(f"{ans[i].name} {ans[i].score1} {ans[i].score2} {ans[i].score3}")