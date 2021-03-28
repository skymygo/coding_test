def solution(numbers, target):
    datas = [0]
    for i in numbers:
        datas = [_+i for _ in datas] + [ _ - i for _ in datas]
    datas = [_ for _ in datas if _ == target]
    return len(datas)

if __name__ == '__main__':
    input = [[[1, 1, 1, 1, 1],3]]
    output = [5]
    

    for _input, _output in zip(input, output):
        pred = solution(*_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))