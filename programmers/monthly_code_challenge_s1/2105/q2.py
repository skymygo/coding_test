from collections import Counter
def solution1(numbers):
    answer = []
    for number in numbers:
        i = 1
        while True:
            out = number ^ (number+i)
            c = Counter(bin(out))
            if c.get("1") < 3:
                answer.append(number+i)
                break
            i+=1

    return answer

def solution(numbers):
    answer = []
    for number in numbers:
        number_str = bin(number)[2:]
        if "0" in number_str:
            zero_pos = (len(number_str) - number_str[::-1].index("0")) -1
            new_number_str = number_str[:zero_pos] + "1"
            if zero_pos < len(number_str)-1:
                new_number_str += "0" + number_str[zero_pos+2:]
            number_str = new_number_str
        else:
            number_str = "10"+ number_str[1:]
        answer.append(int("0b"+number_str, 2))

    return answer

if __name__ == '__main__':
    _in =[
        [2,7]
        ]
    _out = [
        [3,11]
    ]

    for _input, _output in zip(_in ,_out):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred == _output, _input, _output, pred))