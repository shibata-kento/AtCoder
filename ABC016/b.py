a, b, c = map(int, input().split())
if a + b == c:
    if a - b == c:
        print('?')
        exit()
    else:
        print('+')
        exit()
elif a - b == c:
    print('-')
    exit()
else:
    print('!')