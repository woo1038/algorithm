# 14659 한조서열정리하고옴ㅋㅋ

n = int(input())
h = list(map(int, input().split()))

cnt = 0
result = 0
max_num = 0

for i in h:
    if i > result:
        result = i
        cnt = 0
    else:
        cnt += 1

    max_num = max(cnt, max_num)

print(max_num)