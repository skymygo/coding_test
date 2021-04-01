import math

def solution(distance, rocks, n):
    min_dis, max_dis = 0, distance
    rocks = sorted(rocks)

    while min_dis != max_dis:
        points = [0] + rocks + [distance]
        mid = math.ceil((min_dis + max_dis) / 2)
        pos = 0
        while pos < len(points)-1:
            if points[pos+1] - points[pos] < mid:
                del points[pos+1]
                if len(points) < len(rocks) + 2 - n:
                    break;
            else:
                 pos+=1

        if points[-1] - points[-2] < mid:
            del points[-2]
        if len(points) >= len(rocks)+2 -n:
            if min_dis == mid:
                min_dis = max_dis
            else:
                min_dis = mid
        else:
            if max_dis == mid:
                max_dis = min_dis
            else:
                max_dis = mid

    return min_dis

if __name__ == '__main__':
    input = [[25,[2, 14, 11, 21, 17],2], [25,[5, 11, 14, 17, 20],2]]
    output = [4, 5]

    for _input, _output in zip(input, output):
        pred = solution(*_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred == _output, _input, _output, pred))