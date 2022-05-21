n = int(input())
m = int(input())
s = []
a = 0
for i in range(n):               # создает матрицу и перобразует str в int
    s.append(input().split())
    for j in range(m):
        s[i][j] = int(s[i][j])
c = max(s[0])
for i in range(n):
    if c < max(s[i]):
        c = max(s[i])
        a = i
print(a, s[a].index(c))