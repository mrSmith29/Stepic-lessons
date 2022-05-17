line = input().split()
num = int(input())


def chunked(s, n):
    list1 = []
    while len(s) != 0:
        list1.append(s[:n])
        s = s[n:]
    return list1


print(chunked(line, num))
