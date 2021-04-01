def solution(n, stations, w):
    area = [0] * n
    for stt in stations:
        for i in range(stt-1-w,stt+w if stt+w < n else n):
            area[i] =1
    answer = 0
    pos = 0
    while pos < n:
        if area[pos] == 0:
            answer+=1
            pos += w*2+1
        else:
            pos +=1
    return answer

import math
def solution(n, stations, w):
    answer = 0
    pre = 1
    for pos in stations:
        answer += math.ceil(((pos-w - pre-1) / ((2*w)+1)))
        pre = pos+w

    answer += math.ceil((n-pre) / ((2*w)+1))

    return answer


if __name__ == '__main__':
    input = [[11,[4, 11],1], [16,[9],2]]
    output = [3, 3]

    for _input, _output in zip(input, output):
        pred = solution(*_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))