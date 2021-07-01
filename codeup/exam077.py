a = int(input())
hap = 0

# for i in range(0, a + 1):
#     if i % 2 == 0:
#         hap = hap + i

while a > 0:
    if a % 2 == 0:
        hap = hap + a
    a = a - 1

print(hap)
