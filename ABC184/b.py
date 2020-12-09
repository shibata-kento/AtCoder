n, x = map(int, input().split())
s = input()
for i in range(len(s)):
    if s[i] == 'x':
        if x != 0:
            x -= 1
    else:
        x += 1
print(x)