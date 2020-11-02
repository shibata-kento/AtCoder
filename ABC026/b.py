import math
n = int(input())
r = [int(input())**2 for i in range(n)]
r.sort()
circle = 0
for i in range(n):
    if i % 2 == 0:
        circle += r[i]
    else:
        circle -= r[i]
print(abs(circle * math.pi))