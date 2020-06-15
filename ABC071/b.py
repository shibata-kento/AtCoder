s = list(input())
exist = 'abcdefghijklmnopqrstuvwxyz'

j = 0
s = set(s)
s = sorted(s)
if len(s) == 26:
    print('None')
    exit()
for i in range(len(s)+1):
    try:
        if s[i] == exist[j]:
            pass    
        elif s[i] != exist[j]:
            print(exist[j])
            break
        j += 1
    except:
        print('z')

