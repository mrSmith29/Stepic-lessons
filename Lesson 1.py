s = input().split() + [' ']
c = []
list1 = []
for i in range(len(s) - 1):
    list1.append(s[i])
    if s[i] != s[i + 1]:
        c.append(list1)
        list1 = []

print(c)


