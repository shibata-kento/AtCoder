n = int(input())

i = 1
tmp = []
while i * i <= n:
    if n % i == 0:
        tmp.append(i)
        tmp.append(n//i)
    i += 1
tmp = sorted(list(set(tmp)))
for i in range(len(tmp)):
    print(tmp[i])