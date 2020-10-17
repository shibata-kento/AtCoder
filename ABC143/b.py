n = int(input())
d = list(map(int, input().split()))
k = d[1:]
c = 0
for i in range(n):
    for j in range(len(k)):
        c += d[i] * k[j]
    k = k[1:]
print(c)   