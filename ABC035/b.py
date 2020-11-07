s = input()
t = int(input())
x, y, c = 0, 0, 0
for i in s:
    if i == 'L':
        x -= 1
    elif i == 'R':
        x += 1
    elif i == 'U':
        y += 1
    elif i == 'D':
        y -= 1
    elif i == '?':
        c += 1
xy = abs(x) + abs(y)
if t == 1:
    print(xy+c)
else:
    if xy < c:
        if(c-xy) % 2 == 0:
            print(0)
        else:
            print(1)
    else:
        print(xy - c)
#??