s = input()
c = 0
if s[0] == 'R':
    c += 1
    if s[1] == 'R':
        c += 1
        if s[2] == 'R':
            c += 1
else:
    if s[1] == 'R':
        c += 1
        if s[2] == 'R':
            c += 1
    else:
        if s[2] == 'R':
            c += 1
print(c)
