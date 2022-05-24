n = int(input())
m = int(input())
def matrix(n, m):
    s = []
    for i in range(n):               # создает матрицу
        s.append(input().split())
    return s

c = matrix(n,m)
a = input().split()
for i in c:
    i[int(a[0])], i[int(a[1])] = i[int(a[1])], i[int(a[0])]
    print(* i)