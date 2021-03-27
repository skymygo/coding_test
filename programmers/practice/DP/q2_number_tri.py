def solution(triangle):
    for _row in range(len(triangle)-1, 0, -1):
        for _col in range(len(triangle[_row-1])):
            triangle[_row-1][_col] += triangle[_row][_col] if triangle[_row][_col] > triangle[_row][_col+1] else triangle[_row][_col+1]

    answer = triangle[0][0]
    return answer


if __name__ == '__main__':
    input = [[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]]
    output = [30]

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))