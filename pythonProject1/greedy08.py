# 18238 ZOAC 2

words = input()
cnt = 0
start = 'A'

for word in words:
    left = ord(start) - ord(word)
    right = ord(word) - ord(start)

    if left < 0:
        left += 26
    if right < 0:
        right += 26

    cnt += min(left, right)
    start = word

print(cnt)