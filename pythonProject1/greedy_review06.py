# 곱하기 혹은 더하기

n = list(input())
result = 1

for i in n:
    if int(i) == 0:
        result += int(i)
    else:
        result *= int(i)

print(result)

