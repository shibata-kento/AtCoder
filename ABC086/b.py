a, b = map(int, input().split())
num = int(str(a) + str(b))
i = 0
while i*i <= 100100:
    if num == i*i:
        print('Yes')
        exit()
    i += 1
print('No')