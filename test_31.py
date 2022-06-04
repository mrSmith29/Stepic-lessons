n = input()
s=[]
for i in range(8):
    s.append(['.' for i in range (8)])
c = 'abcdefgh'
s[8 - int(n[1])][c.find(n[0])] = 'Q'
a = 8 - int(n[1])
b = c.find(n[0])
for i in range(8):
    for j in range(8):
        if i == 8 - int(n[1]) and j != c.find(n[0]):
            s[i][j] = '*'
        if j == c.find(n[0]) and i != 8 - int(n[1]):
            s[i][j] = '*'

for i in range(a - 1, -1, -1):
    if b < 7:
        b += 1
        s[i][b] = '*'
a = 8 - int(n[1])
b = c.find(n[0])
for i in range(a - 1, -1, -1):
    if b > 0:
        b -= 1
        s[i][b] = '*'

a = 8 - int(n[1])
b = c.find(n[0])
for i in range(a + 1, 8):
    if b < 7:
        b += 1
        s[i][b] = '*'

a = 8 - int(n[1])
b = c.find(n[0])
for i in range(a + 1, 8):
    if b > 0:
        b -= 1
        s[i][b] = '*'
for i in range(8):
    for j in range(8):
        print(str(s[i][j]).ljust(2), end='')
    print()
