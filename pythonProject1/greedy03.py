# 1434 책 정리

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

hap_a = 0
hap_b = 0

for x in a:
    hap_a += x

for y in b:
    hap_b += y

result = hap_a - hap_b
print(result)