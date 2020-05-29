n, m = map(int, input().split())
if n*2 >= m:
    result = m//2
else:
    result = (m - n*2)//4 + n
print(result)