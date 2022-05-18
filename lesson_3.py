s = input().split()
list1 = [[]] + [[i] for i in s]
a = 2
list2 = []
if len(s) != 1:
    for i in range(len(s)):
        list2.append(s[i:i + a])
    while a != len(s):
        a += 1
        for i in range(len(s)):
            list2.append(s[i:i + a])

    for i in list2:
        if i not in list1:
            list1.append(i)
else:
    list2 = [[],[s[0]]]
print(list1)





