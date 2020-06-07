n = int(input())
s = []
for i in range(5):
    s.append(input())
start = 0
end = 4
out = ''
for i in range(n):
    result = ''
    nt = []

    for j in range(5):
        nt.append(s[j][start:end])

    result = ''.join(nt)
    num = result.count('#')
    start = end
    end += 4

    if num == 12:
        if result[13] == '#':
            if result[7] == '#':
                out += '0'
            else:
                out += '6'
        else:
            out += '9'
    elif num == 8:
        out += '1'
    elif num == 11:
        if result[13] == '#':
            out += '2'
        elif result[5] == '.':
            out += '3'
        else:
            out += '5'
    elif num == 9:
        out += '4'
    elif num == 7:
        out += '7'
    elif num == 13:
        out += '8'

print(out)
