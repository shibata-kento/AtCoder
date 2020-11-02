s = input()
n = int(input())
c = 0
for i in range(len(s)):
    for j in range(len(s)):
        string = f'{s[i]}{s[j]}'
        c += 1
        if c == n:
            print(string)
            exit()
