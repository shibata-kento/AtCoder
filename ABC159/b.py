s = input()
slen = len(s)
if s == s[::-1]:
    sln1 = (slen-1)//2
    sn1 = s[0:sln1]
    if sn1 == sn1[::-1]:
        sln3 = (slen+3)//2
        sn3 = s[sln3-1:slen]
        if sn3 == sn3[::-1]:
            print('Yes')
            exit()
print('No')
