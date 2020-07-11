n = int(input())
c = [0]*n
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            N = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if n >= N:
                c[N-1] += 1
for i in c:
    print(i)
