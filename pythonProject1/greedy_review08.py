# 만들수 없는 금액
import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, input().split())), reverse=True)
cnt = 0
result = 0


while True:
    cnt += 1
    result = cnt

    for i in a:
        if result >= i:
            result -= i
            if result == 0:
                break

    if result > 0:
        break

print(cnt)