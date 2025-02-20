c_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

def number_to_str(num):
    res = ''
    while num > 0:
        res += c_list[num % len(c_list)-1]
        num = (num-1) //len(c_list)
    return res[::-1]

def str_to_number(s):
    res = 0
    for c in s:
        res *= len(c_list)
        res += c_list.index(c)+1

    return res

def solution(n, bans):
    bans = [str_to_number(_) for _ in bans]
    bans.sort()
    for b in bans:
        if n >= b:
            n+=1
        else:
            break
    return number_to_str(n)

print(solution(30, ["d", "e", "bb", "aa", "ae", 'ba']))


# aad =[f"{_}" for _ in c_list]
# aad += [f"{_}{__}" for _ in c_list for __ in c_list]
# aad += [ f"{_}{__}{___}" for _ in c_list for __ in c_list for ___ in c_list]
# for i, num in enumerate(aad):
#     print(i+1, num, str_to_number(num), number_to_str(i+1))
#
# # print(str_to_number("aaa"))
# print(number_to_str(26))