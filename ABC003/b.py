s = input()
t = input()
string = ['a', 't', 'c', 'o', 'd', 'e', 'r']
for i in range(len(s)):
    stmp = True
    ttmp = True
    if s[i] == t[i]:
        continue
    if s[i] == '@':
        stmp = t[i] in string
    elif t[i] == '@':
        ttmp = s[i] in string
    elif s[i] != t[i]:
        print('You will lose')
        exit()      
    if stmp == False or ttmp == False:
        print('You will lose')
        exit()
print('You can win')