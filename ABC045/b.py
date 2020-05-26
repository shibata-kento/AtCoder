def del_flg(X, person, flg = 0):
    try:
        person = X[0]
        X = X[1:]
    except:
        flg = 1

    return person, X, flg

A = list(input())
B = list(input())
C = list(input())
flg = 0

al = len(A) + len(B) + len(C)
person = 'a'
flg = ''
for i in range(al):
    if person == 'a':
        person, A, flg = del_flg(A, person)
    elif person == 'b':
        person, B, flg = del_flg(B, person)
    else:
        person, C, flg = del_flg(C, person)

    if flg == 1:
        break

print(person.upper())
