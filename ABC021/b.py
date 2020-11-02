n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))
flg = False
if a in p or b in p:
    flg = True
if len(p) != len(set(p)) or flg == True:
    print('NO')
    exit()
print('YES')