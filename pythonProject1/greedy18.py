# 1543번 문서 검색

n = input()
word = input()

n = n.replace(word, "@")
print(n.count("@"))

