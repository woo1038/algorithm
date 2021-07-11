# 10809 알파벳 찾기
import sys

# a = str(sys.stdin.readline().rstrip())
# print(a)
# cnt = -1
# arr = [str(-1) for _ in range(26)]
#
# for i in n:
#     cnt += 1
#     if arr[ord(i) - ord("a")] != str(-1):
#         arr[ord(i) - ord("a")] = str(cnt -1)
#     else:
#         arr[ord(i) - ord("a")] = str(cnt)
#
#
# print(' '.join(arr))



n = list(map(str, input()))
alpha = list('abcdefghijklmnopqrstuvwxyz')
arr = [-1 for _ in range(len(alpha))]

for i in range(len(n)):
    if arr[alpha.index(n[i])] == -1:
        arr[alpha.index(n[i])] = i

for j in arr:
    print(j, end=" ")
