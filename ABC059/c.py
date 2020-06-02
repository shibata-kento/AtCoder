#??


n = int(input())
al = list(map(int, input().split()))

def calc(al, p_n):
    result = 0
    total = 0
    for a in al:
        total += a
        if total * p_n < 1:
            result += abs(p_n - total)
            total = p_n
        p_n = p_n*-1
    return result

print(min(calc(al, 1), calc(al, -1)))