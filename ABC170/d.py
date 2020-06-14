n = int(input())
a = list(map(int, input().split()))
amin = min(a)
if amin > n:
    print(0)
else:
    print(n+1 - min(a))
