def solution(n, t, m, p):
    strings = ''
    count = 0
    while len(strings) < t * m:
        new_i = count
        new_strings = ''
        if new_i == 0:
            new_strings += '0'
        while new_i > 0:
            new_strings += str(hex(new_i % n)).split('0x')[-1].upper()
            new_i //= n
        strings += new_strings[::-1]
        count +=1

    answer = strings[p-1::m]
    return answer[:t]

print(solution(2,4,2,1))