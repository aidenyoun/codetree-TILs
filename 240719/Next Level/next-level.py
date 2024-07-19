class Status:
    def __init__(self, user_id = "codetree", level = 10):
        self.user_id = user_id
        self.level = level
temp = input().split()
status1 = Status()
print(f"user {status1.user_id} lv {status1.level}")
status1 = Status(temp[0], temp[1])
print(f"user {status1.user_id} lv {status1.level}")