n = int(input())
result = n % 1000

if result > 0:
    print(1000 - result)
else:
    print(result)
