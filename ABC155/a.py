a, b, c = map(int, input().split())
if a == c and a != b:
    print('Yes')
elif b == c and a != b:
    print('Yes')
elif a == b and b != c:
    print('Yes')
else:
    print('No')