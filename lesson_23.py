num = input().split()
s = [i for i in range(1, (int(num[0]) * int(num[1])) + 1)]
c = [[] for i in range(int(num[0]))]
start = 0
for i in range(int(num[0])):
    for j in range(start,len(s), int(num[0])):
        c[i].append(s[j])
    start += 1
    for g in range(int(num[1])):
        print(str(c[i][g]).ljust(3), end = '')
    print()

