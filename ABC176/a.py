n, x, t = map(int, input().split())
if n % x == 0:
    tako = n // x
else:
    tako = n // x + 1
print(tako * t)