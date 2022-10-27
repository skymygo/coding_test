def solution_1(a, b):
    answer = a
    for _ in range(b-1):
        print(answer)
        answer *= a
        answer = answer%100000

    return answer

def solution_2(a, b):
    a = a % 100000
    answer = 1
    res_dict = dict()
    for _ in range(b):
        if answer not in res_dict:
            res_dict[answer] = (answer * a ) % 100000
        answer = res_dict[answer]

    return answer

def solution(a, b):
    a = a % 100000
    answer = a
    res_list = [(1,a)]
    pow_count =1
    while pow_count < b:
        if pow_count + res_list[-1][0] > b:
            res_list = [_ for _ in res_list if pow_count + _[0] <= b]
        answer = (answer * res_list[-1][1]) % 100000
        pow_count += res_list[-1][0]
        res_list.append((pow_count, answer))

    return answer

if __name__ == '__main__':
    in_out = [[2, 26, 8864]]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))