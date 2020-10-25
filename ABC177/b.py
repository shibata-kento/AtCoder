s = input()
t = input()
st = len(s) * len(t)
if t in s:
    print(0)
    exit()
else:
    for i in range(len(s) - len(t) + 1):
        c = 0
        tmp = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                tmp += 1
        c = st
        if c > tmp:
            st = tmp
print(st)