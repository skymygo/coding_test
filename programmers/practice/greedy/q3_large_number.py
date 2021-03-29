def solution_1(number, k):
    pos = 0
    number = list(number)
    while k > 0 and pos < len(number) - 1:
        if number[pos] < number[pos + 1]:
            del number[pos]
            k -= 1
            pos -= 1
        else:
            pos += 1
    if k > 0 and number[-1] < number[-2]:
        del number[-1]
        k -= 1

    return ''.join(number[k:])

def solution(number, k):
    answer = ''
    number = list(number)
    pos = 0
    while k < len(number)-pos:
        max = number[pos]
        idx = 0
        for _pos in range(pos, pos+k+1):
            if max < number[_pos]:
                max = number[_pos]
                idx = _pos-pos
            if max == "9": break;
        answer += max
        pos += idx+1
        k -= idx
    return answer

if __name__ == '__main__':
    input = [["1924", 2], ["1231234",3], ["4177252841",4]]
    output = ["94", "3234", "775841"]

    for _input, _output in zip(input, output):
        res = solution(*_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

