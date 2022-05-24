n = int(input())
s = [input().split() for _ in range(n)]
s.reverse()
for i in s:
    print(*i)