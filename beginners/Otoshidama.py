n, y = map(int, input().split())
show = '-1 -1 -1'
for i in range(n+1):
    for j in range(n+1):
        k = n - i - j
        total = i*10000 + j*5000 + k*1000
        if k < 0:
            break 
        if total == y:
            show = '{} {} {}'.format(i, j, k)
            break
        else:
            continue
  

print(show)