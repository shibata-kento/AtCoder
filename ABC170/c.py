x, n = map(int, input().split())
p = list(map(int, input().split()))
if p == []:
    print(x)
    exit()
t = [0]*(max(p)+2)
for i in p:
    t[i] = 1

mi = t[:x+1]
ma = t[x:]
mi.reverse()
mii = mi.index(0)
maa = ma.index(0)

if mii < maa:
    print(x-mii)
elif mii > maa:
    print(x+maa)
elif mii == maa:
    print(x-mii)