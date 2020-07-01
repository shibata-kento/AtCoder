n, y = map(int, input().split())
for a in range(n+1):
    for b in range(n+1):
        c = n - (a+b)
        if a*10000 + b*5000 + c*1000 == y and a+b+c == n and c >= 0:
            print(a, b, c)
            exit()
print('-1 -1 -1')