n = int(input())
a = list(map(int, input().split()))
seta = list(set(a))

if len(seta) == 1:
    print(0)
elif sum(a) % n > 0:
    print(-1)
else:
    c = 0
    ans = 0
    ap = sum(a)/n
    for i in range(n-1):
        if a[i] == ap:
            continue
        elif a[i] > ap:
            ans += 1
            a[i+1] += a[i]-ap
            a[i] = ap
        elif a[i] < ap:
            ans += 1
            a[i+1] -= ap-a[i]
            a[i] = ap
    print(ans)