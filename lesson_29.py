num = input().split()
s = [[0 for _ in range(int(num[1]))] for _ in range(int(num[0]))]
c = [[0 for _ in range(int(num[0]))] for _ in range(int(num[1]))]
a = 1
d = []
for i in range(1):
    for j in range(len(s[0])):
        s[i][j] = a
        a += 1
print(*s, sep='\n' )
for i in range(int(num[1]) - 1, -1, -1):
    for j in range(int(num[0])):
