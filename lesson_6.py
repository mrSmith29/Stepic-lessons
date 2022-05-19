n = int(input())
s = [input().split() for _ in range(n)]
sl = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sl += int(s[i][j])
print(sl)

