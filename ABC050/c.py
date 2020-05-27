n = int(input())
a = list(map(int, input().split()))
s = set(a)
limit = 10**9+7

if sum(a) == 2 * sum(s):
    print(2**(n//2)%limit)
else:
    print(0)
    