def solution(dice):

    _max = dice[0][0]
    _min = dice[0][1]

    for d in dice:
        _max = max([_max]+d)
        _min = min([_min]+d)



    answer = []
    return answer


solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])