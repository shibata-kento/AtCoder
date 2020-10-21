x = int(input())
yen = 100
c = 0
while x > yen:
    yen = int(yen*1.01)
    c += 1
print(c)