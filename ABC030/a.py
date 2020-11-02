a, b, c, d = map(int, input().split())
ab, cd = b/a, d/c
if ab > cd:
    print('TAKAHASHI')
elif ab < cd:
    print('AOKI')
elif ab == cd:
    print('DRAW')