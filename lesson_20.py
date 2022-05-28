num = input().split()
s = []
for i in range(1, int(num[0]) + 1):
    c = []
    for j in range(1, int(num[1]) + 1):
        if j % 2 == 0 and i % 2 != 0 :
            c.append('*')
        elif j % 2 != 0 and i % 2 == 0:
            c.append('*')
        else:
            c.append('.')
    s.append(c)
for i in s:
    print(*i)