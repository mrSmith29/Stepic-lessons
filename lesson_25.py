n = int(input())
s = [[1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i > j and i < n - 1 - j) or (i < j and i > n - 1 - j):
            s[i][j] = 0
        print(str(s[i][j]).ljust(3), end='')
    print()