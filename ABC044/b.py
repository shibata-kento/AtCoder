w = input()
duplex = set(w)
before_w = ''
result = 'Yes'
diff = 0
for i in duplex:
    before_w = w.replace(i, '')
    diff = diff + (len(w) - len(before_w))
    w = before_w
    if diff % 2 == 0:
        pass
    else:
        result = 'No'
        break

print(result)
