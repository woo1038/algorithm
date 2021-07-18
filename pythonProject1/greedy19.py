# 1758 알바생 강호

n = int(input())
a = sorted([int(input()) for _ in range(n)], reverse=True)
sum = 0

for idx, val in enumerate(a):
    if val - ((idx + 1) - 1) > 0:
        sum += val - ((idx + 1) - 1)

print(sum)

