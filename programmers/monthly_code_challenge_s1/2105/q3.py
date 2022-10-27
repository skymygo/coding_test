def solution1(s):
    answer = []
    for number in s:
        pos, i = 0, 0
        while i < len(number)-2:
            if number[i:i+3] == '110':
                while pos < i:
                    if number[pos:pos+3] == '111':
                        number = number[:pos] + '110' + number[pos:i] + number[i+3:]
                        i -=3
                    pos+=1
            i+=1
        answer.append(number)
    return answer

def solution(s):
    answer = []
    for number in s:
        pos = 0
        while pos < len(number)-2:
            if "110" not in number[pos:]:
                break
            pos = pos + number[pos:].index("110")
            if "111" in number[:pos+2]:
                pos1 = number[:pos+2].index("111")
                number = number[:pos1] + '110' + number[pos1:pos] + number[pos + 3:]
                pos -=2

        answer.append(number)

    return answer

if __name__ == '__main__':
    _in =[
        ["1110","100111100","0111111010", "110000"]
        ]
    _out = [
        ["1101","100110110","0110110111", "000110"]
    ]

    for _input, _output in zip(_in ,_out):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred == _output, _input, _output, pred))

    # print('0110110'.index('110'))