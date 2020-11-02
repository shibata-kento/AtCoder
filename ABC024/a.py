a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
if s+t >= k:
    c = c*(s+t)
    print(a*s + b*t - c)
else:
    print(a*s + b*t)
