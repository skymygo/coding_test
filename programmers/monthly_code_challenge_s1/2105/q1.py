import math


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        if (math.sqrt(i)) %1:
            answer += i
        else:
            answer -= i
    return answer

if __name__ == '__main__':
    _in =[
        [13,17]
        ]
    _out = [
        43
    ]

    for _input, _output in zip(_in ,_out):
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred == _output, _input, _output, pred))