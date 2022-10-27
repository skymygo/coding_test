def solution(rows, columns, queries):
    answer = []
    mat_val = [[row*rows + col+1 for col in range(columns)] for row in range(rows)]

    for query in queries:
        query = [_-1 for _ in query]
        x1,y1, x2,y2 = query

        min_value = mat_val[x1][y1]
        init_value = mat_val[x1][y1]
        for i in range(x1,x2):
            mat_val[i][y1] = mat_val[i+1][y1]
            min_value = min(min_value, mat_val[i][y1])
        for i in range(y1,y2):
            mat_val[x2][i] = mat_val[x2][i+1]
            min_value = min(min_value, mat_val[x2][i])
        for i in range(x2,x1,-1):
            mat_val[i][y2] = mat_val[i-1][y2]
            min_value = min(min_value, mat_val[i][y2])
        for i in range(y2,y1,-1):
            mat_val[x1][i] = mat_val[x1][i-1]
            min_value = min(min_value, mat_val[x1][i])
        mat_val[x1][y1+1] = init_value

        answer.append(min_value)

    return answer

if __name__ == '__main__':
    input = [[6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]], [3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]], [100,97,[[1,1,100,97]]]]
    output = [[8, 10, 25], [1, 1, 5, 3], [1]]

    for _input, _output in zip(input[1:],output):
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))
        import sys; sys.exit()
