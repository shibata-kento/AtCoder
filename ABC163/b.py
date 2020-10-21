n, m = map(int, input().split())
a = list(map(int, input().split()))
flg = n - sum(a)
if flg < 0:
    print(-1)
else:
    print(flg)