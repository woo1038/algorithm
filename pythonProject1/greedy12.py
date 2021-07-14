# 14655 욱제는 도박쟁이야!!

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += abs(a[i])
    sum += abs(b[i])

print(sum)
