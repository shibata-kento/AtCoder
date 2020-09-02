h, w = map(int, input().split())
a = [input() for i in range(h)]
for i in range(h):
    tmp = ''
    if a[i].count('.') != w:
        for j in range(w):
            tmp += a[j][i]
        if '#' in tmp:
            print(a[i])