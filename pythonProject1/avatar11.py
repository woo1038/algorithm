# 15552 빠른 A+B
import sys

n = int(sys.stdin.readline().rstrip())

print(n)
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)