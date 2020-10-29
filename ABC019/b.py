s = input()
tmp = ''
c = 1
string = ''
for i in range(len(s)-1):
    tmp = s[i]
    if tmp == s[i+1]:
        c += 1
    else:
        string += str(tmp) + str(c)
        c = 1
if s[-1] == s[-2]:
    string += s[-1] + str(c)
else:
    string += s[-1] + '1'
print(string)
