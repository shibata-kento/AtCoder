n = int(input())
a = list(map(int, input().split()))
a.sort()

c = a[-1] - a[0]
print(c)