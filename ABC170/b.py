x, y = map(int, input().split())
result = 'No'
for i in range(x+1):
    t = x-i
    k = x-t
    if y == t*2 + k*4:
        result = 'Yes'
        break
print(result)