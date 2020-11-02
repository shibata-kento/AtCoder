n, m = map(int, input().split())
if n > 12:
    n -= 12
N = 30 * n + 0.5 * m
M = 6 * m
angle = abs(N-M)
if angle >= 180:
    print(360-angle)
else:
    print(angle)
#??