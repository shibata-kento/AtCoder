import math

a = int(input())
b = int(input())
n = int(input())
N = (a*b) // math.gcd(a, b)
for i in range(0, 20001+N, N):
    if i >= n:
        print(i)
        exit()
    
