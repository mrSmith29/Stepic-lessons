n = int(input())
s = [input().split() for _ in range(n)]
c = []
for i in range(len(s)):                 #преобразование элементов str в int
    for j in range(len(s[i])):
        s[i][j] = int(s[i][j])

for i in range(n):
    for j in range(len(s[i])):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            c.append(s[i][j])
print(c)
print(max(c))