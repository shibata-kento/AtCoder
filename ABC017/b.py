choku = ['ch', 'o', 'k', 'u']
x = input()
for i in range(4):
    x = x.replace(choku[i], '')
if len(x) == 0:
    print('YES')
else:
    print('NO')