y, x = map(int, input().split())
a  = []
cnt = 0
num = 0

for i in range(y):
    a.append([])
    for k in range(x):
        a[i].append(0)

for i in range(y):
    cnt += 1

    num = cnt + (y * (x-1))
    for k in range(x):
        a[i][k] = num
        num -= y


for i in range(y):
    print(a[i])

# n, m = map(int, input().split())
#
# for i in range(n - 1, -1, -1):
#     for j in range(0, n * m, n):
#         print(n * m - i - j, end=' ')
#     print()