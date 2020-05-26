n = int(input())
a = list(map(int, input().split()))
c = 0

while all(b % 2 == 0 for b in a ):
    a = [b/2 for b in a]
    c += 1

print(c)