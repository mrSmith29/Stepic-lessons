n = int(input())
s = [['.' for _ in range(n)] for j in range(n)]
for i in range(len(s)):
    s[i][n - i - 1] = '1'
    for j in range(len(s)):
        if s[i][j] != '1' and j < n - i - 1:
            s[i][j] = '0'
        elif s[i][j] != '1' and j > n - i - 1:
            s[i][j] = '2'

for i in s:
    print(*i)
