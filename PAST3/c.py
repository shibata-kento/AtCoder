a, r, n = map(int, input().split())
large = 10**9
if r == 1:
    print(a)
    exit()
if n >= 31:
    print('large')
    exit()

for i in range(n-1):
    a *= r
    if a > large:
        print('large')
        exit()
print(a)