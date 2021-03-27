def solution(m, n, puddles):
    routes = [ [0 for _ in range(m)] for __ in range(n)]
    routes[0][0] = 1
    for pr, pl in puddles:
        routes[pl-1][pr-1] = None
    for row in range(n):
        for col in range(m):
            if routes[row][col] is None: routes[row][col] =0
            elif row == 0 and col == 0:continue
            else:
                routes[row][col] = (routes[row-1][col] if row != 0 else 0) + (routes[row][col-1] if col != 0 else 0)

    answer = routes[-1][-1] % 1000000007
    return answer

if __name__ == '__main__':
    input = [[4, 3, [[2, 2]]]]
    output = [4]

    for _input, _output in zip(input, output):
        pred = solution(*_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))