n, k = map(int, input().split())
h = list(map(int, input().split()))
c = 0
for i in range(n):
    if k <= h[i]:
        c += 1
print(c)