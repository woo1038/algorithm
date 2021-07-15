# 9237 이장님 초대

n = int(input())
tree = sorted(list(map(int, input().split())), reverse=True)

for i in range(len(tree)):
    tree[i] += i + 2

print(max(tree))