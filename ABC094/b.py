n, m, x = map(int, input().split())
a = list(map(int, input().split()))
ans = [0]*(n+1)
for i in a:
    ans[i] = 1

print(min(sum(ans[:x]), sum(ans[x+1:])))
