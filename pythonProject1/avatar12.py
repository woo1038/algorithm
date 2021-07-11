# 8958 OX퀴즈
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    cnt = 0
    result = 0

    a = list(map(str, sys.stdin.readline().rstrip()))
    for k in range(len(a)):
        if a[k] == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0

    print(result)