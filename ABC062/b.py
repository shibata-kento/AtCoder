h, w = map(int, input().split())
for i in range(h+2):
    result = ''
    result += '#'
    if i == 0 or i == h+1:
        result *= w+2
    else:
        a = input()
        result += a + '#'
    print(result)
            