# 5585 거스름돈

n = int(input())

coins = [500, 100, 50, 10, 5, 1]
pay = 1000 - n
result = 0

for coin in coins:
    result += pay // coin
    pay %= coin

print(result)