st = input().split()
n = int(input())
a = -1
s = [[] for _ in range(n)]
for i in range(n):
    a += 1
    for j in range(a,len(st), n):
        s[i].append(st[j])
print(s)