n, k = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
result = 0
for i in range(k):
    result += p[i]

print(result)