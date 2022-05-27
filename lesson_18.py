n = input()
s=[]
for i in range(12):
    s.append(['.' for i in range (12)])
c = '..abcdefgh..'
s[12 - (int(n[1])) - 2][c.find(n[0])] = 'N'
s[(12 - (int(n[1])) - 2) + 2][c.find(n[0]) + 1] = '*'
s[(12 - (int(n[1])) - 2) + 2][c.find(n[0]) - 1] = '*'
s[(12 - (int(n[1])) - 2) + 1][c.find(n[0]) + 2] = '*'
s[(12 - (int(n[1])) - 2) + 1][c.find(n[0]) - 2] = '*'
s[(12 - (int(n[1])) - 2) - 2][c.find(n[0]) + 1] = '*'
s[(12 - (int(n[1])) - 2) - 2][c.find(n[0]) - 1] = '*'
s[(12 - (int(n[1])) - 2) - 1][c.find(n[0]) + 2] = '*'
s[(12 - (int(n[1])) - 2) - 1][c.find(n[0]) - 2] = '*'

for i in s[2:10]:
    print(* i[2:10])
