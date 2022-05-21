n = int(input())
s = [input().split() for _ in range(n)]


for i in range(len(s)):                 #преобразование элементов str в int
    for j in range(len(s[i])):
        s[i][j] = int(s[i][j])

for i in range(len(s)):
    total = 0
    for j in s[i]:
        if j > sum(s[i]) / len(s[i]):
            total += 1
    print(total)
