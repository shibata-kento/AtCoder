s = input()
t = input()
ans = 10**9
string = ''
if t in s:
    print(0)
else:
    for i in range(len(s) - len(t) + 1):
        string = s[i:i+len(t)]
        c = 0
        for  j, k in enumerate(string):
            if t[j] != k:
                c += 1
        ans = min(ans, c)
print(ans)
