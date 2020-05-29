# ??

from itertools import permutations

n, m = map(int, input().split())
diff = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    diff[a-1][b-1] = 1
    diff[b-1][a-1] = 1

result = 0
for j in permutations(range(1, n)):
    j = [0] + list(j)
    cnt = 1
    for k in range(n-1):
        if diff[j[k]][j[k+1]] == 0:
            cnt = 0
    result += cnt

print(result)