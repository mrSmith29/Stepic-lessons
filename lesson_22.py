num = input().split()
s = [i for i in range(1, (int(num[0]) * int(num[1])) + 1) ]
c = []
for i in range(int(num[0])):
    c.append(s[:int(num[1])])
    s = s[int(num[1]):]

for i in range(int(num[0])):
    for j in range(int(num[1])):
        print(str(c[i][j]).ljust(3), end = '')
    print()