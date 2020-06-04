n, m = map(int, input().split())
result = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    result[a-1] += 1
    result[b-1] += 1

for j in result:
    print(j)

