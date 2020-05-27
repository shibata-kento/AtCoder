w, h, n = map(int, input().split())
b = 0
l = 0

for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        l = max(l, x)
    elif a == 2:
        w = min(w, x)
    elif a == 3:
        b = max(b, y)
    else:
        h = min(h, y)

print(max(h - b, 0)*max(w - l, 0))