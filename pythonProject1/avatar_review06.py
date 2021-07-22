# 문자열 재정렬

n = sorted(list(input()))

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = 0
slic = 0

for i in n:
    for k in num:
        if i == str(k):
            cnt += int(i)
            slic += 1

del n[0:slic]
n.append(str(cnt))
a = "".join(n)

print(a)