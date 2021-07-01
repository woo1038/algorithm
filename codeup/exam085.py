h, b, c = map(int, input().split())
bit = h*b*c/8/1024/1024
print('%0.2f MB' % bit)
