# 상하좌우
import sys

n = int(sys.stdin.readline())
x, y = 1, 1
plans = sys.stdin.readline().split()


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
moves = ["R", "L", "U", "D"]

for plan in plans:
    for move in range(len(moves)):
        if moves[move] == plan:
            nx = x + dx[move]
            ny = y + dy[move]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny


print(x, y)
