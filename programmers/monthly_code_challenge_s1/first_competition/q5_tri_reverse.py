def solution(n):
    answer = tri_to_dec(str(int(dec_to_tri(n)[::-1])))

    return answer

def dec_to_tri(n):
    answer = ''
    while n>0:
        answer = str(n%3) + answer
        n = n//3
    return answer

def tri_to_dec(n):
    answer= 0
    for i in list(n):
        answer = answer *3
        answer += int(i)
    return answer


if __name__ == '__main__':
    in_out = [[45, 7], [125,229]]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))