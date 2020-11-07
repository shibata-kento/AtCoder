n = int(input())
squ = ['']*n
for i in range(n):
    tmp = input()
    for j in range(n):
        squ[j] += tmp[j]

for i in range(n):
    print(squ[i][::-1])