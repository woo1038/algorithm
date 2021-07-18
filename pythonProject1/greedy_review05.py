# 모험가 길드

n = int(input())
x = sorted(list(map(int, input().split())), reverse=True)
num = 0
cnt = 0

while True:
    if len(x) == 0:
        break

    del x[0:int(x[0])]
    cnt += 1

print(cnt)
