s = input()
sl = len(s) - 1
loop = 2 ** sl
total = 0
for i in range(loop):
    x = ''
    for index, num in enumerate(s):
        x += num
        if (i >> index) & 1:
            x += '+'

    total += eval(x)

print(total)
