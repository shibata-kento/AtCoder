n, d = map(int, input().split())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
c = 0
for i in range(n):
    for j in range(i+1, n):
        tmp = 0
        for k in range(d):
            tmp += abs(x[i][k] - x[j][k])**2
        tmp = tmp**0.5
        if str(tmp)[-2:] == '.0':
            c += 1
print(c)
