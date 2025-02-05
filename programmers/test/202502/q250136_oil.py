def oil_sum(land, row, col, index):
    cur_oil = 1
    stack = [(row, col)]
    history = []
    max_row = len(land)
    max_col = len(land[0])

    land[row][col] = 0
    while stack:
        cur_spot = stack.pop()
        history.append(cur_spot)
        if max_row > cur_spot[0]+1 and land[cur_spot[0]+1][cur_spot[1]] == 1:
            land[cur_spot[0]+1][cur_spot[1]] = 0
            cur_oil += 1
            stack.append((cur_spot[0]+1, cur_spot[1]))
        if max_col > cur_spot[1]+1 and land[cur_spot[0]][cur_spot[1]+1] == 1:
            land[cur_spot[0]][cur_spot[1]+1] = 0
            cur_oil += 1
            stack.append((cur_spot[0], cur_spot[1]+1))

        if 0 < cur_spot[0] and land[cur_spot[0]-1][cur_spot[1]] == 1:
            land[cur_spot[0]-1][cur_spot[1]] = 0
            cur_oil += 1
            stack.append((cur_spot[0]-1, cur_spot[1]))
        if 0 < cur_spot[1] and land[cur_spot[0]][cur_spot[1]-1] == 1:
            land[cur_spot[0]][cur_spot[1]-1] = 0
            cur_oil += 1
            stack.append((cur_spot[0], cur_spot[1]-1))

    for h in history:
        land[h[0]][h[1]] = (cur_oil, index)


def solution(land):
    answer = 0
    index = 0

    for row in range(len(land)):
        for col in range(len(land[0])):
            if land[row][col] == 1:
                oil_sum(land, row, col, index)
                index += 1

    for i in range(len(land[0])):
        sum_oil = 0
        index_list = []
        for j in range(len(land)):
            if land[j][i] != 0 and land[j][i][1] not in index_list:
                sum_oil += land[j][i][0]
                index_list.append(land[j][i][1])
        answer = max(sum_oil, answer)

    return answer


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print(solution([[1,1,1,1,1],[1,0,0,0,0],[1,0,0,1,0],[1,0,0,0,0],[1,1,1,1,1]]))
print(solution([[1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0]]))