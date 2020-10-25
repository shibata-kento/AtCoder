n = int(input())
a, b, c = 0, 0, 1
if n < 3:
    print(0)
else:
    for i in range(2, n-1):
        a, b, c = b, c, (a+b+c)%10007
    print(c)