n = int(input())
lst = []
i = 1

while n != 0:
    if n - i > i:
        n -= i
        lst.append(i)
        i += 1
    else:
        lst.append(n)
        n = 0

print(len(lst))
for j in lst:
    print(j, end=' ')