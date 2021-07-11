# 2562 최댓값
import sys

# arr = [int(input()) for _ in range(9)]

arr = []
for i in range(9):
    a = int(sys.stdin.readline())
    arr.append(a)

print(max(arr), arr.index(max(arr))+1)



