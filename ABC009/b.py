n = int(input())
a = [int(input())]
for i in range(n-1):
    tmp = int(input())
    flg = tmp in a
    if flg == False:
        a.append(tmp)
a.sort()
if len(a) == 1:
    print(a[0])
else:
    print(a[-2])