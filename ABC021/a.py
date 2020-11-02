n = int(input())
num = [8, 4, 2, 1]
l = []
c = 0
while n != 0:
    for N in num:
        if n - N < 0:
            continue
        else:
            n -= N
            l.append(N)
        c += 1
print(c)
for i in l:
    print(i)