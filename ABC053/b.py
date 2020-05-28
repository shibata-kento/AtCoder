s = list(input())
start = s.index('A')
s.reverse()
end = len(s) - s.index('Z')

print(end - start)