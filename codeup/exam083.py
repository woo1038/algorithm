r, g, b = map(int, input().split())
cnt = 0
for i in range(0, r):
    for k in range(0, g):
        for j in range(0, b):
            print(i, k, j)
            cnt += 1
print(cnt)
