def solution(bricks):
    answer = 0
    l = 0
    r = len(bricks)-1
    l_value = bricks[l]
    r_value = bricks[r]
    while l<r:
        if l_value < r_value:
            l +=1
            if l_value > bricks[l]:
                answer += l_value - bricks[l]
            else:
                l_value = bricks[l]
        else:
            r -=1
            if r_value > bricks[r]:
                answer += r_value - bricks[r]
            else:
                r_value = bricks[r]
    return answer

if __name__ == '__main__':
    in_out = [[[0, 2, 0, 1, 3, 1, 2, 0, 1, 0, 2, 0],9], [[1, 2, 3, 4, 5, 6, 7],0]]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(_input[0])
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))