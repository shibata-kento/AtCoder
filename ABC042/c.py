n, k = map(int,input().split())
d = set(input().split())
 
while True:
    for c in str(n):
        if c in d:
            break
    else:
        print(n)
        exit()
    n += 1