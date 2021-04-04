def solution(n, costs):
    answer = [None] * n
    data_queue = [[0,0]]
    pos = 0
    while len(data_queue) > pos:
        island, cost = data_queue[pos]
        pos +=1
        if answer[island] is None or answer[island] > cost:
            answer[island] = cost
        else:
            continue
        _costs = [ [_[1], _[2]] for _ in costs if _[0] == island and (answer[_[1]] is None or answer[_[1]] < _[2] ) ]
        _costs2 =[ [_[0], _[2]] for _ in costs if _[1] == island and (answer[_[0]] is None or answer[_[0]] < _[2] ) ]
        data_queue.extend(_costs)
        data_queue.extend(_costs2)

    return sum(answer)


if __name__ == '__main__':
    input = [[4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]]]
    output = [4]

    for _input, _output in zip(input, output):
        res = solution(*_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

