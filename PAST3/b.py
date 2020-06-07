n, m, q = map(int, input().split())

nl = [[] for _ in range(n)]
ml = [n for _ in range(m)]

for i in range(q):
    s = list(map(int, input().split()))
    total = 0
    person_num = s[1] - 1
    if s[0] == 2:
        question_num = s[2] - 1
        nl[person_num].append(s[2])
        ml[question_num] -= 1
    else:
        if nl[person_num] == []:
            print('0')
        else:
            for j in nl[person_num]:
                total += ml[j-1]
            print(total)        
