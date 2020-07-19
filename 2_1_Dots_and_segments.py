from operator import itemgetter

cuts = []
n = int(input())
for i in range(n):
    cut = tuple(map(int, input().split()))
    cuts.append(cut)
cuts = sorted(cuts, key=itemgetter(1, 0))

points = [cuts[0][1]]
for cut in cuts:
    if points[-1] < cut[0]:
        points.append(cut[1])

print(len(points))
for i in points:
    print(i, end=' ')