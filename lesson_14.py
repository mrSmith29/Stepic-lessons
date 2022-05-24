n = int(input())
s = [input().split() for _ in range(n)]
flag = 0
for i in range(n):
    for j in range(n):
        if s[i][j] != s[j][i]:
            flag = 1
if flag == 0:
    print('YES')
else:
    print('NO')


