n = int(input())
c = 1
if n < 3:
    print(n)
    exit()

for i in range(6):
    c = c*2
    if n < c*2:
        print(c)
        break
