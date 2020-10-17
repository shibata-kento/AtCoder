n, k, m = map(int, input().split())
a = list(map(int, input().split()))
asum = sum(a)
for i in range(k+1):
    if (asum+i) // n >= m:
        print(i)
        exit()
print(-1)