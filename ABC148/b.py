n = int(input())
s, t = input().split()
string = ''
for i in range(n):
    string += s[i] + t[i]
print(string)