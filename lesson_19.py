n = int(input())
s = [input().split() for _ in range(n)]
c = [int(j) for i in s for j in i]
for i in s:                     #преобразование  str в int
    for j in range(len(i)):
        i[j] = int(i[j])
sm = sum(s[0])
s.extend([[], []])
for i in range(n):                          #создает список  включений для магического квадрата
    s[n].append(s[i][i])
    s[n + 1].append(s[i][n - i - 1])
    d = []
    for j in range(n):
        d.append(s[j][i])
    s.append(d)

def includ():
    for i in range(1,n ** 2 + 1):
        if i not in c:
            flag = False
            break                 #проверяет содержит ли матрица числа от 1 до n ** 2
        else:
            flag = True
    return flag

def total():
    for i in range(len(s)):
        if sum(s[i]) != sm:
            flag = False
            break
        else:
            flag = True
    return flag

if includ() == False or total() == False:
    print('NO')
else:
    print('YES')

