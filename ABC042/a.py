num = list(map(int, input().split()))
result = 'YES'
try:
    num.remove(5)
    num.remove(7)
    num.remove(5)
except:
    pass
    result = 'NO'

print(result)
