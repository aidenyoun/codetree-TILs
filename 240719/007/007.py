class Secret:
    def __init__(self, code, where, time):
        self.code = code
        self.where = where
        self.time = time

secret1_temp = input().split()
secret1 = Secret(secret1_temp[0], secret1_temp[1], secret1_temp[2])
print(f"secret code : {secret1_temp[0]}")
print(f"meeting point : {secret1_temp[1]}")
print(f"time : {secret1_temp[2]}")