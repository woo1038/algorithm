a = int(input())

for i in range(1, a + 1):
    str_a = str(i)
    cnt = 0
    for x in str_a:
        if (x == '3') or (x == '6') or (x == '9'):
            cnt += 1
    if cnt == 0:
        print(i, end=' ')
    else:
        print(cnt * '짝', end=' ')

