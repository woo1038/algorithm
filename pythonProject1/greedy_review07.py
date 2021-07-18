# 문자열 뒤집기

n = list(str(input()))
zero = 0
one = 0

if int(n[0]) == 0:
    zero += 1
else:
    one += 1

for i in range(0, len(n)-1):
    if int(n[i]) == int(n[i+1]):
        continue

    if int(n[i]) != int(n[i+1]):
        if int(n[i+1]) == 0:
            zero += 1
        elif int(n[i+1]) == 1:
            one += 1

print(min(zero, one))