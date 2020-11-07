n = int(input())
mp = 0
ap = []
vi = []
for i in range(n):
    s, p = input().split()
    ap.append(int(p))
    vi.append(s)
    mp = max(mp, int(p))
if mp <= sum(ap)//2:
    print('atcoder')
else:
    name = ap.index(mp)
    print(vi[name])
