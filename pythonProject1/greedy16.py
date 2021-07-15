# 1789번 수들의 합

s = int(input())
count = 0
hap = 0
result = 0

while s > hap:
    count += 1
    hap += count

    if hap > s:
        result = count - 1

    if hap == s:
        result = count

print(result)
