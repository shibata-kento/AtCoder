alpha = ['A', 'B', 'C', 'D', 'E', 'F']
s = input()
c = [0]*6
for i in s:
    tmp = alpha.index(i)
    c[tmp] += 1
print(*c)