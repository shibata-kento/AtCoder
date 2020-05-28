n, m = map(int, input().split())
for _ in range(n):
    a = list(input())
for _ in range(m):
    b = list(input())
result = []

for i in range(n-m+1):
    for j in range(n-m+1):
        for k in range(m):
            result.append(a[j+k][i:i+m])
        if b == result:
            print('Yes')
            exit()

print('No')
