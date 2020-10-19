n = int(input())
x = list(map(int, input().split()))
ma = 0
yu = 0
che = 0
for i in range(n):
    ma += abs(x[i])
    yu += abs(x[i]**2)
    che = max(abs(che), abs(x[i]))
print(ma)
print(yu**0.5)
print(che)