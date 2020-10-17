alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n = int(input())
s = input()
string = ''
for i in range(len(s)):
    tmp = (alpha.index(s[i]) + n) % 26
    string += alpha[tmp]

print(string)
