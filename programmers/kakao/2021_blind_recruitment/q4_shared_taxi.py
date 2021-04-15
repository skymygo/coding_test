from queue import PriorityQueue
def solution(n, s, a, b, fares):
    fares.extend([[_[1], _[0], _[2]] for _ in fares])
    start_to_min = [-1] * n
    que = PriorityQueue()
    que.put((0,s-1))
    while que.qsize() >0:
        fare, start = que.get()
        if start_to_min[start] == -1 or start_to_min[start] > fare:
            start_to_min[start] = fare
            for _ in [_ for _ in fares if _[0] == start+1]:
                que.put((fare+_[2], _[1]-1))

    min_value = start_to_min[a-1] + start_to_min[b-1]

    distance_with_index = [(value,num) for num, value in enumerate(start_to_min) if value >0]
    distance_with_index.sort(key= lambda x:x[0])

    for fare, start in distance_with_index:
        if min_value <= fare: break
        que.put((0, start))
        start_to_min = [-1] * n
        while que.qsize() > 0:
            fare1, start1 = que.get()
            if start_to_min[start1] == -1 or start_to_min[start1] > fare1:
                start_to_min[start1] = fare1
                for _ in [_ for _ in fares if _[0] == start1 + 1]:
                    que.put((fare1 + _[2], _[1] - 1))
        if min_value > fare + start_to_min[a-1] + start_to_min[b-1]:
            min_value = fare + start_to_min[a-1] + start_to_min[b-1]

    return min_value

if __name__ == '__main__':
    in_out = [
        [6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]], 82],
        [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]], 14],
        [6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]], 18]
    ]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))