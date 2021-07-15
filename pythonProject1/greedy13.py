# 15720 카우버거

n = list(map(int, input().split()))
b = sorted(list(map(int, input().split())), reverse=True)
c = sorted(list(map(int, input().split())), reverse=True)
d = sorted(list(map(int, input().split())), reverse=True)

result = 0
cnt = 0
num = 0

num = sum(b) + sum(c) + sum(d)

minValue = min(len(b), len(c), len(d))

for _ in range(minValue):
    result += (b[0] + c[0] + d[0]) * 0.9
    b.pop(0)
    c.pop(0)
    d.pop(0)

for k in range(len(b)):
    result += b[k]

for k in range(len(c)):
    result += c[k]

for k in range(len(d)):
    result += d[k]


print(num)
print(int(result))