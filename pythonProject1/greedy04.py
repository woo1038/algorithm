# 2810 컵 홀더

n = int(input())
member = input()
count = member.count('LL')

if count <= 1:
    print(len(member))
else:
    print(len(member) - count + 1)