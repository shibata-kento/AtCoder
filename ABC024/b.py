n, t = map(int, input().split())
a = [int(input()) for i in range(n)]
T = 0
for i in range(n-1):
    if a[i+1] - a[i] < t:
        T += a[i+1] - a[i]
    else:
        T += t
print(T + t)