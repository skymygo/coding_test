def solution(s):
    if len(s)%2 ==1:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1:len(s)//2+1]


if __name__ == '__main__':
    in_out = [["abcde", "c"], ["qwer", "we"]]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))