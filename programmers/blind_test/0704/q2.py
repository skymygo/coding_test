def solution(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==0 and j==0:
                pass
            elif i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    answer = grid[len(grid)-1][len(grid[0])-1]
    return answer


if __name__ == '__main__':
    input = [[ [1, 2], [3, 4] ],
             [ [1, 8, 3, 2], [7, 4, 6, 5] ]
             ]
    output = [7,19]

    for _input, _output in zip(input[:],output):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))
