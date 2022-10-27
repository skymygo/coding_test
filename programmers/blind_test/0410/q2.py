def solution_1(foods):
    answer = 0
    for pos in range(1, len(foods)):
        sum1 = sum(foods[:pos])
        sum2 = 0
        for pos2 in range(pos, len(foods)):
            sum2 += foods[pos2]
            if sum1 == sum2:
                if sum2 == sum(foods[pos2+1:]):
                    answer+=1

    return answer

def solution_2(foods):
    answer = 0
    for pos in range(1, len(foods)):
        sum1 = sum(foods[:pos])
        sum2 = sum(foods[pos:])
        if sum1*2 != sum2:continue

        sum2 = foods[pos]
        sum3 = sum(foods[pos+1:])
        if sum1 == sum2: answer +=1

        for pos2 in range(pos+1, len(foods)):
            sum2 += foods[pos2]
            sum3 -= foods[pos2]
            if sum1 == sum2: answer+=1

    return answer


def solution(foods):
    answer = 0
    sum1 = 0
    sum1_2 = sum(foods)
    for pos in range(0, len(foods)):
        sum1 += foods[pos]
        sum1_2 -= foods[pos]
        if sum1*2 != sum1_2:continue

        sum2 = foods[pos+1]
        sum3 = sum(foods[pos+2:])
        if sum1 == sum2: answer +=1

        for pos2 in range(pos+2, len(foods)):
            sum2 += foods[pos2]
            sum3 -= foods[pos2]
            if sum1 == sum2: answer+=1

    return answer


if __name__ == '__main__':
    in_out = [[[1,2,3,0,3],2], [[4,1],0]]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(_input[0])
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))