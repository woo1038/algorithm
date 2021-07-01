n = int(input())
a = list(map(int, input().split()))
b = a[0]

for i in range(n):
    if b > a[i]:
        b = a[i]
print(b)