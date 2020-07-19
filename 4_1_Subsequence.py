n = int(input())
a = [int(i) for i in input().split()]
d = [0] * n

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] <= a[i] and a[i] % a[j] == 0 and d[j] + 1 > d[i]:
            d[i] = d[j] + 1

ans = 0
for i in range(n):
    ans = max(ans, d[i])

print(ans)