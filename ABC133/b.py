n, d = map(int, input().split())
c = 0
check = []
x = [list(map(int, input().split())) for i in range(n)]
for i in range(n-1):
    tmp = []
    for j in range(d):
        tmp.append(abs(x[i][j] - x[i+1][j])**2)
    check.append(str(sum(tmp)**0.5))
    if check[-1][-1] == '0':
        c += 1
for j in range(d):
    tmp.append(abs(x[n-1][j] - x[0][j])**2)
check.append(str(sum(tmp)**0.5))
if check[-1][-1] == '0':
    c += 1 

print(c)

????