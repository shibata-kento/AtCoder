# ??
n = int(input())
a = list(map(int, input().split()))
al = [0]*(10**5+2)

for i in a:
    al[i] += 1
    al[i+1] += 1
    al[i+2] += 1

print(max(al))