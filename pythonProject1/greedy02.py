# 2720 세탁소 사장 동혁

t = int(input())

coins = [25, 10, 5, 1]

for i in range(t):
    pay = int(input())
    count = 0

    for coin in coins:
        count = pay // coin
        pay %= coin
        print(count, end=' ')

    print(sep='\n')

