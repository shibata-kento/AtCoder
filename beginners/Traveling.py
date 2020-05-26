n = int(input())
t, x, y = 0, 0, 0

for i in range(n):
    t1, x1, y1 = map(int, input().split())
    diff = abs(x1 - x) + abs(y1 - y)
    if diff > (t1 - t) or (diff - (t1 - t)) % 2 == 1:
        print('No')
        exit()
    t, x, y = t1, x1, y1

print('Yes')