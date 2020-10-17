a, b = map(int, input().split())
if a == b:
    print(str(a)*b)
else:
    print(str(min(a,b))*max(a,b))