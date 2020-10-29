s = input()
n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    tmp = s[l-1:r][::-1]
    s = s[:l-1] + tmp + s[r:]
print(s) 
