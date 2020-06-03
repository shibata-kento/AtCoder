n, t = map(int, input().split())
total, prev = 0, 0
for tl in map(int, input().split()):
    total += min(tl - prev, t)
    prev = tl
print(total + t)