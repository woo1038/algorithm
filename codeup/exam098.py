a = []

for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)

for x in range(10):
    n = list(map(int, input().split()))
    for y in range(10):
        a[x][y] = n[y]

cnt = 1
twobreak = True
for x in range(1, 9):
    for y in range(1, 9):
        if a[x][cnt] == 2:
            a[x][cnt] = 9
            twobreak = False
            break
        if a[x][cnt+1] == 0:
            a[x][cnt] = 9
            cnt += 1
        if a[x][cnt+1] == 1:
            a[x][cnt] = 9
            break
    if twobreak == False:
        break


for i in range(10):
    print(a[i])