n, k = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l, reverse=True)
result = 0
for i in range(k):
    result += l[i]
print(result)