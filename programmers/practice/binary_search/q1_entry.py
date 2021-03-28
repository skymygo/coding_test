def solution(n, times):
    answer = 0
    return answer


if __name__ == '__main__':
    input = [[6, [7,10]]]
    output = [28]

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred == _output, _input, _output, pred))