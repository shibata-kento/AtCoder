o = input()
e = input()
string = len(o) + len(e)
result = ''
c = 0
for i in range(string):
    try:
        result += o[i]
    except:
        pass
    try:
        result += e[i]
    except:
        pass
print(result)