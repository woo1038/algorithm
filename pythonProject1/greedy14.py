# 1343 폴리오미노

# n = list(map(str, input().split()))
# list = []
# list2 = []
# result = 0
#
#
# for item in n:
#     a = item.replace("XX", "BB")
#     list.append(a)
#
# for item in list:
#     a = item.replace("BBBB", "AAAA")
#     list2.append(a)
#
# for item in list2:
#     for i in range(len(item)):
#         if item[i] == "X":
#             result = -1
#             break
#
# if result != 0:
#     print(result)
# else:
#     print(list2[0])

n = input()

n = n.replace("XXXX", "AAAA")
n = n.replace("XX", "BB")

if "X" in n:
    print(-1)
else:
    print(n)
