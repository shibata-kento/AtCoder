a, b, c, k = map(int, input().split())
if a+b < k:
    sub = abs(a+b-k)
    print(a-sub)
elif k <= a:
    print(k)
else:
    print(a)