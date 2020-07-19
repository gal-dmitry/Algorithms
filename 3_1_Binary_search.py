a = []
for i in input().split():
    a.append(int(i))
n = a[0]
a.remove(n)

b = []
for i in input().split():
    b.append(int(i))
k = b[0]
b.remove(k)

for i in range(k):
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == b[i]:
            print(m + 1, end=" ")
            break
        elif a[m] > b[i]:
            r = m - 1
        else:
            l = m + 1
    if l > r:
        print('-1', end=" ")