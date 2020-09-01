n = int(input())
c = 0
for i in range(1, n+1, 2):
    tmp = 0
    for j in range(1, n+1, 2):
        if i % j == 0:
            tmp += 1
    if tmp == 8:
        c += 1
print(c)