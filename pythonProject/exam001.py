n = 1260
cnt = 0

arr = [500, 100, 50, 10]

for i in arr:
    cnt += n // i
    n %= i

print(cnt)