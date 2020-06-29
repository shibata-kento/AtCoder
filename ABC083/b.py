n, a, b = map(int, input().split())
less = []
for i in range(a, n+1):
    num = 0
    digit = len(str(i))
    if digit > 1:
        string = str(i)
        for j in range(digit):
            num += int(string[j])
    else:
        num = i

    if a <= num <= b:
        less.append(i)

print(sum(less))