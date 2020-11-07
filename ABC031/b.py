l, h = map(int, input().split())
n = int(input())
for i in range(n):
    a = int(input())
    if a < l:
        print(l-a)
    elif l <= a <= h:
        print(0)
    elif h < a:
        print(-1)