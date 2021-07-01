a = []
w, h = map(int, input().split())

for i in range(w):
    a.append([])
    for k in range(h):
        a[i].append(0)


c = int(input())
for i in range(c):
    l, d, x, y = map(int, input().split())

    if d == 0:
        for k in range(l):
            if a[x-1][k] == 0: a[x-1][k] = 1
    elif d == 1:
        for j in range(l):
            if a[j+1][y-1] == 0: a[j+1][y-1] = 1


for i in range(5):
    print(a[i])