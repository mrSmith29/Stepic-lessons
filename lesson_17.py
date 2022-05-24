n = int(input())
s = [input().split() for _ in range(n)]
for i in range(n):
    c = []
    for j in range(len(s) - 1, -1, -1):
        c.append(s[j][i])
    print(*c)
