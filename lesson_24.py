n = int(input())
list = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    list[i][i] = 1
    list[i][n - i -1] = 1
    for j in range(n):
        print(str(list[i][j]).ljust(3), end='')
    print()

