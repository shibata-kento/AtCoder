w = input()
aiueo = ['a', 'i', 'u', 'e', 'o']
a = ''
for i in w:
    flg = i in aiueo
    if flg == False:
        a += i
print(a)   
