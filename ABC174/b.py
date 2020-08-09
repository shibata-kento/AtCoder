n, d = map(int, input().split())
c = 0
for i in range(n):
    x, y = map(int, input().split())
    ans = (x**2 + y**2) ** 0.5
    if ans <= d:
        c += 1
print(c)