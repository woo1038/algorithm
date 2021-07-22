# 럭키 스트레이트

n = list(input())
result = ""
cnt = 0

if len(n) % 2 == 0:
    for i in range(len(n) // 2):
        cnt += int(n[i])
    for k in range(len(n) // 2, len(n)):
        cnt -= int(n[k])
    if cnt == 0:
        result = "LUCKY"
    else:
        result = "READY"
else:
    result = "READY"

print(result)