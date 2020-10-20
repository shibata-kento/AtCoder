a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
n = int(input())
A1 = [0,0,0]
A2 = [0,0,0]
A3 = [0,0,0]
 
for i in range(n):
    b = int(input())
    try:
        tmp = a1.index(b)
        A1[tmp] += 1
    except:
        pass
    try:
        tmp = a2.index(b)
        A2[tmp] += 1
    except:
        pass
    try:
        tmp = a3.index(b)
        A3[tmp] += 1
    except:
        pass
if sum(A1) == 3 or sum(A2) == 3 or sum(A3) == 3 or A1[0] + A2[0] + A3[0] == 3 or A1[1] + A2[1] + A3[1] == 3 or A1[2] + A2[2] + A3[2] == 3 or A1[0] + A2[1] + A3[2] == 3 or A1[2] + A2[1] + A3[0] == 3:
    print('Yes')
else:
    print('No')