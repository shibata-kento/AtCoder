n, k = map(int, input().split())
treat = []
for i in range(k):
    d = int(input())
    a = input()
    if len(a) != 1:
        tmp = ''
        for j in a:
            if j != ' ':
                tmp += j
            else:
                treat.append(int(tmp))
                tmp = ''
        treat.append(int(tmp))
    else:
        treat.append(int(a))
treat = set(treat)
print(n - len(treat))