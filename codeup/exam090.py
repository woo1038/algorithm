a, b, c, d = map(int, input().split())

hap = a
for i in range(a+1 , d+1):
    hap = hap * b + c

print(hap)