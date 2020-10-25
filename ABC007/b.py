alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = input()
if len(a) > 1:
    print(a[:-1])
else:
    tmp = alpha.index(a)
    if tmp != 0:
        print(alpha[tmp-1])
    else:
        print(-1)