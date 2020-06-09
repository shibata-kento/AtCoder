n = int(input())
a = [int(input()) for _ in range(n)]
now = a[0]
c = 1

if now == 2:
    print(1)
    exit()

for i in range(n):
    now = a[now-1]
    c += 1
    if now == 2:
        print(c)
        exit()
print(-1)