a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
flg = 1
if a > b:
    flg = -1

a = a+v*t*flg
b = b+w*t*flg

if flg == 1:
    if a >= b:
        print('YES')
    else:
        print('NO')
else:
    if a <= b:
        print('YES')
    else:
        print('NO')