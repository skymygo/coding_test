def solution(n):
    answer = 0

    return answer

if __name__ == '__main__':
    input = [4]
    output = [11]

    for _input, _output in zip(input,output):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))