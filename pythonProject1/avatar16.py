# 10809 알파벳 찾기

# alpha = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:')
# print(alpha[alpha.index("H")])

n = int(input())

for i in range(n):
    r, s = input().split()

    text = ""

    for s in s:
        text += int(r) * s

    print(text)