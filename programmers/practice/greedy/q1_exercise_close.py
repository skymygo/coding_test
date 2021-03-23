def solution(n, lost, reserve):
    answer = n
    _reserve = set(reserve)
    lost = set(lost)
    reserve = _reserve - lost
    lost = lost - _reserve
    for lost_student in lost:
        if lost_student-1 in reserve:
            reserve.remove(lost_student-1)
        elif lost_student+1 in reserve:
            reserve.remove(lost_student+1)
        else:
            answer -= 1

    return answer


if __name__ == '__main__':
    input = [[5,[2,4],[1,3,5]], [5,[2,4],[3]], [3,[3],[1]]]
    output = [5,4,2]

    for i in range(len(input)):
        res = solution(input[i][0], input[i][1], input[i][2])
        print('{}, input: {}, output: {}, predict: {}'.format(res==output[i], input, output, res))

