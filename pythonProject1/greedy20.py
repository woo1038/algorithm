# 1417번 국회의원 선거
import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

da = a[0]
a.pop(0)
cnt = 0

while True:
    a.sort(reverse=True)
    if da <= a[0]:
        cnt += 1
        da += 1
        a[0] -= 1
    else:
        break

print(cnt)
