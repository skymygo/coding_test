def solution(numbers):

    numbers = set((total_number(numbers)))
    answer = 0
    print(numbers)
    for i in numbers:
        if int(i) > 1 and is_prime_number(i):
            print(i)
            answer+=1

    return answer

def total_number(numbers):
    data_stack = [['',numbers]]
    res = list()
    while(len(data_stack) > 0):
        _input_number, data_number = data_stack.pop()
        if _input_number != '':
            res.append(int(_input_number))
        if (len(data_number) == 1):
            res.append(int(_input_number+data_number[0]))
        else:
            for i in range(len(data_number)):
                data_stack.append([_input_number + data_number[i], data_number[:i]+data_number[i+1:]])
    return res

def is_prime_number(number):
    number = int(number)
    max_num = round(pow(number, 0.5))+1
    for i in range(2,max_num):
        if number % i == 0: return False

    return True


if __name__ == '__main__':
    input = ['17', '011', '0121']
    output = [3,2, 1]

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred == _output, _input, _output, pred))