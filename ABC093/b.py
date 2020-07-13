a, b, k = map(int, input().split())
if b-a >= k*2: 
    for i in range(k):
        print(a+i)

    for j in range(-k+1, 1):
        print(b+j)

else:
    for i in range(0, b-a+1):
        print(a+i)
