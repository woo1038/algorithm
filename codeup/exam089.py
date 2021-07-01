a, b, c = map(int, input().split())
cnt = 1
hap = a

while cnt < c:
    cnt += 1
    hap = hap * b

print(hap)