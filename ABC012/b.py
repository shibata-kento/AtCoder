n = int(input())
H, M, S = 0, 0, 0
if n >= 3600:
    H = n // 3600
    n -= 3600 * (n//3600)

if n >= 60:
    M = n // 60
    n -= 60 * (n//60)

S = n
print('{:02}:{:02}:{:02}'.format(H, M, S))