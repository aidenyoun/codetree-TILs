class Codename:
    def __init__(self, name, score):
        self.name = name
        self.score = score

score_list = []
for i in range(5):
    name, score = tuple(input().split())
    score_list.append(Codename(name, int(score)))

score_list.sort(key=lambda x: x.score)
print(f"{score_list[0].name} {score_list[0].score}")