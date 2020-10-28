n, x = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    if (x >> i) & 1 == 1:
        c += a[i]

print(c)
# ??