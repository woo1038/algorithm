n = int(input())
pan = []



for i in range(19):
    pan.append([])
    for j in range(19):
        pan[i].append(0)

for i in range(n):
    x, y = map(int, input().split())
    pan[x-1][y-1] = 1

for i in range(19):
    print(pan[i])

