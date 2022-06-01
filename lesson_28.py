num = input().split()
s = [[i for i in range(1, int(num[1]) + 1)] for _ in range(int(num[0]))]
nm = 0
for i in range(int(num[0]) * int(num[1])):
    for j in range(int(num[0])):
        for k in range(int(num[1])):
            if j + k == i:
                nm += 1
                s[j][k] = nm

for i in range(int(num[0])):
    for j in range(int(num[1])):
        print(str(s[i][j]).ljust(3), end='')
    print()
