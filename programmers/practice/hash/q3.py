def solution(clothes):
    clothes_dict = dict()
    for cloth in clothes:
        if clothes_dict.get(cloth[1], 0) == 0:
            clothes_dict[cloth[1]] = 1
        else:
            clothes_dict[cloth[1]] += 1

    answer = 1
    for key,value in clothes_dict.items():
        answer *= (value+1)

    return answer-1