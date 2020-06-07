s = input()
t = input()

if s.upper() == t.upper():
    if s == t:
        print('same')
    else:
        print('case-insensitive')
else:
    print('different')