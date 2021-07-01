a = []
for i in range(19):
    a.append([])
    for k in range(19):
        a[i].append(0)


for i in range(19):
    b = input().split()
    for k in range(19):
        a[i][k] = int(b[k])

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for k in range(19):
        if a[k][y-1] == 0: a[k][y-1] = 1
        else: a[k][y-1] = 0

        if a[x-1][k] == 0: a[x-1][k] = 1
        else: a[x-1][k] = 0


for i in range(19):
    print(a[i])
