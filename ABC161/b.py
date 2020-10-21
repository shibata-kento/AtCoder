n, m = map(int, input().split())
a = list(map(int, input().split()))
popular = sum(a) / (4*m)
for i in range(n):
    if a[i] >= popular:
        m -= 1
if m <= 0:
    print('Yes')
else:
    print('No')
