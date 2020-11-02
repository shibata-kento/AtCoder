n, s, t = map(int, input().split())
w = int(input())
a = [int(input()) for i in range(n-1)]
if s <= w <= t:
    c = 1
else:
    c = 0
for i in range(n-1):
    w += a[i]
    if s <= w <= t:
        c += 1

print(c)
