from collections import Counter
def solution(n, edge):
    answer = [n] * n
    graph = [[] for _ in range(n+1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    data_queue = [[[1],0]]
    pos = 0
    while len(data_queue) > pos:
        starts, cost = data_queue[pos]
        pos += 1
        for start in starts:
            if answer[start-1] > cost:
                answer[start-1] = cost
                data_queue.append([graph[start], cost+1])
    c = Counter(answer)
    return c[max(c.keys())]

if __name__ == '__main__':
    input = [[6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]]]
    output = [3]

    for _input, _output in zip(input, output):
        res = solution(*_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

