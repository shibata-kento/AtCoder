s = input()
k = int(input())
slen = len(s)
if slen < k:
    print(0)
    exit()
else:
    c = 0
    num = []
    for i in range(slen+1):
        if s[i:i+k] not in num and i+k <= slen:
            num.append(s[i:i+k])
            c += 1
print(c)