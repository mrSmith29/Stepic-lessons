n = int(input())
s = [input().split() for _ in range(n)]
c1 = []
c2 = []
c3 = []
c4 = []

for i in range(len(s)):                 #преобразование элементов str в int
    for j in range(len(s[i])):
        s[i][j] = int(s[i][j])

for i in range(n):
    for j in range(len(s[i])):
        if (i < j and i < n - 1 - j):
            c1.append(s[i][j])
        elif (i < j and i > n - 1 - j):
            c2.append(s[i][j])
        elif (i > j and i > n - 1 - j):
            c3.append(s[i][j])
        elif (i > j and i < n - 1 - j):
            c4.append(s[i][j])
print('Верхняя четверть:', sum(c1))
print('Правая четверть:', sum(c2))
print('Нижняя четверть:', sum(c3))
print('Левая четверть:', sum(c4))
