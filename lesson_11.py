n = int(input())
m = int(input())
mult = []
for i in range(n):
    c = []
    for j in range(m):
        c.append(i * j)
    mult.append(c)

for r in range(n):
    for c in range(m):
        print(str(mult[r][c]).ljust(3), end='')
    print()
