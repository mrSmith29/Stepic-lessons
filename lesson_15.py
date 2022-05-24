n = int(input())
s = [input().split() for _ in range(n)]

for i in range(n):
    s[i][i], s[n - i - 1][i] = s[n - i - 1][i], s[i][i]
for i in s:
    print(*i)