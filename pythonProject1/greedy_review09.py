# 볼링공 고르기
import sys

n = sys.stdin.readline()
a = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0

for i in range(len(a)):
    for k in range(i+1, len(a)):
        if a[i] != a[k]:
            cnt += 1

print(cnt)

