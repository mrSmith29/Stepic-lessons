n, m = int(input()), int(input())
s =[]

for _ in range(n):
    s.append([input() for _ in range(m)])

for i in range(n):
    for j in range(m):
        print(s[i][j], end = ' ')
    print()

print()

for i in range(m):
    for j in range(n):
        print(s[j][i], end = ' ')
    print()