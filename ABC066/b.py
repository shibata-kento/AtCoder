s = input()
slen = len(s)
for i in range(1, slen):
    s = s[:-1]
    slen = len(s)
    if i % 2 == 0:
        half = slen // 2
        if s[half:] == s[:half]:
            print(slen)
            break