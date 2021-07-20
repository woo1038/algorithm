# 무지의 먹방 라이브

def solution(foods, k):
    result = 0
    flag = True

    if k > sum(foods):
        return print(-1)

    while flag:
        for i in range(len(foods)):
            if k == 0:
               result = i + 1
               flag = False
               break

            if foods[i] != 0:
                k -= 1
                foods[i] -= 1

    return print(result)


food_tiems = [3, 1, 2]
k = 5

solution(food_tiems, k)