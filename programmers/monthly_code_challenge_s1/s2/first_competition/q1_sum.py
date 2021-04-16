def solution(absolutes, signs):
    num = [num if sign else -num for num, sign in zip(absolutes,signs)]
    return sum(num)

if __name__ == '__main__':
    in_out = [[[4,7,12], [True,False,True], 9], [[1,2,3], [False,False,True],0]]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))