import itertools
n, m = map(int, input().split())
gu = [i for i in range(n)]
ki = [i for i in range(m)]
c = 0
for i in itertools.combinations(gu, 2):
    c += 1
for i in itertools.combinations(ki, 2):
    c += 1
print(c)