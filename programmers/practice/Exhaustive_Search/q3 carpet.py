def solution(brown, yellow):
    width = ((brown-2)/2)-2
    height = 1
    while(width>0):
        if width * height == yellow: break
        width -=1
        height +=1

    answer = [width+2, height+2]
    return answer


if __name__ == '__main__':
    input = [[10,2], [8,1], [24,24]]
    output = [[4,3], [3,3], [8,6]]

    for _input, _output in zip(input, output):
        pred = solution(*_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))