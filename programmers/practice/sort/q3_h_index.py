#1 simple test
def solution(citations):

    citations.sort(reverse=True)
    num = 0
    for num, c in enumerate(citations):
        if c < num: break
    return num

#2 Binary Search
import math
def solution(citations):

    citations.sort(reverse=True)
    start, end = 0, len(citations)
    answer = 0
    while start+1 < end:
        index = math.ceil((start+end) /2)
        if index < citations[index]: start = index; answer =index
        else: end = index

    return answer+1


if __name__ == '__main__':
    input = [[3, 0, 6, 1, 5]]
    output = [3]

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))