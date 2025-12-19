new_tmp = [[val * 3 for val in map(int, input().split())] for _ in range(3)]

for row in new_tmp:
    print(*row)