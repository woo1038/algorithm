# 10162 전자레인지

t = int(input())

button = [300, 60, 10]

for i in button:
    if t % button[2] != 0:
        print(-1)
        break

    count = 0
    count = t // i
    t = t % i


    print(count, end=' ')
