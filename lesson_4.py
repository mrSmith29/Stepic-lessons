n, m = int(input()), int(input())
s =[]

for _ in range(n):
    s.append([input() for _ in range(m)])

for i in range(n):
    for j in range(m):
        print(s[i][j], end = ' ')
    print()
