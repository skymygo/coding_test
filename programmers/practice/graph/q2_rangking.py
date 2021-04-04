def solution(n, results):
    answer = 0
    graph = [[None for _ in range(n)] for __ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for x, y in results:
        graph[x-1][y-1] = 1
        graph[y-1][x-1] = -1



    print(graph)
    return answer
if __name__ == '__main__':
    input = [[5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]]]
    output = [2]

    for _input, _output in zip(input, output):
        res = solution(*_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

