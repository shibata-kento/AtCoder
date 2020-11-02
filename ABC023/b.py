n = int(input())
s = input()
if n % 2 == 0 or s[n//2] != 'b':
    print(-1)
    exit()
elif s == 'b':
    print(0)
    exit()
else:
    c = 1
    string = 'b'
    while c != 102:
        if c % 3 == 1:
            string = f'a{string}c'
        elif c % 3 == 2:
            string = f'c{string}a'
        elif c % 3 == 0:
            string = f'b{string}b'
        if s == string:
            print(c)
            exit()
        c += 1
print(-1)