def solution(numbers):

    print(total_number(numbers))
    answer = 0
    return answer

def total_number(numbers):
    data_stack = [['',numbers]]
    res = list()
    while(len(data_stack) > 0):
        _input_number, data_number = data_stack.pop()
        res.append(_input_number)
        if (len(data_number) == 1):
            res.append(_input_number+data_number[0])
        else:
            for i in range(len(data_number)):
                data_stack.append([_input_number + data_number[i], data_number[:i]+data_number[i+1:]])
    return res


if __name__ == '__main__':
    input = ['17', '011']
    output = [3,2]

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred == _output, _input, _output, pred))