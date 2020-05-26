n, a, b = map(int, input().split())
result = []
for i in range(n + 1):
    if len(str(i)) == 1:
        if a <= i and i <= b:
            result.append(i)
    else:
        string = str(i)
        array = sum(list(map(int, string)))
        if a <= array and array <= b:
            result.append(i)
print(sum(result))