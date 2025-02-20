def select_triangle(grid, spot, line):
    # line 0: top, 1: bottom, 2: left, 3: right
    # 1 = / => lt / rb
    if grid[spot[0]][spot[1]] == 1:
        if line == 0 or line == 2:
            return 0
        else:
            return 1
    else:
        # -1 = \ => lb / rt
        if line == 1 or line == 2:
            return 0
        else:
            return 1


def solution_search(grid, point, spot):
    data_stack = [spot]
    history = set()
    spots = set()
    while data_stack:
        data = data_stack.pop()
        history.add((data[0], data[1]))
        spots.add(data)
        # 1 = / => lt / rb
        if grid[data[0]][data[1]] == 1:
            if data[2] == 0:
                if data[1] > 0:
                    triangle = select_triangle(grid, (data[0], data[1] - 1), 3)
                    new_spot = (data[0], data[1] - 1, triangle)
                    if (new_spot[0], new_spot[1]) not in history:
                        data_stack.append(new_spot)
                if data[0] > 0:
                    triangle = select_triangle(grid, (data[0] - 1, data[1]), 1)
                    new_spot = (data[0] - 1, data[1], triangle)
                    if (new_spot[0], new_spot[1]) not in history:
                        data_stack.append(new_spot)
            else:
                if data[1] < len(grid[0]) - 1:
                    triangle = select_triangle(grid, (data[0], data[1] + 1), 2)
                    new_spot = (data[0], data[1] + 1, triangle)
                    if (new_spot[0], new_spot[1]) not in history:
                        data_stack.append(new_spot)
                if data[0] < len(grid) - 1:
                    triangle = select_triangle(grid, (data[0] + 1, data[1]), 0)
                    new_spot = (data[0] + 1, data[1], triangle)
                    if (new_spot[0], new_spot[1]) not in history:
                        data_stack.append(new_spot)
        # -1 = \ => lb / rt
        if grid[data[0]][data[1]] == -1:
            if data[2] == 0:
                if data[1] > 0:
                    triangle = select_triangle(grid, (data[0], data[1] - 1), 3)
                    new_spot = (data[0], data[1] - 1, triangle)
                    if (new_spot[0], new_spot[1]) not in history:
                        data_stack.append(new_spot)
                if data[0] < len(grid) - 1:
                    triangle = select_triangle(grid, (data[0] + 1, data[1]), 0)
                    new_spot = (data[0] + 1, data[1], triangle)
                    if (new_spot[0], new_spot[1]) not in history:
                        data_stack.append(new_spot)
            else:
                if data[1] < len(grid[0]) - 1:
                    triangle = select_triangle(grid, (data[0], data[1] + 1), 2)
                    new_spot = (data[0], data[1] + 1, triangle)
                    if (new_spot[0], new_spot[1]) not in history:
                        data_stack.append(new_spot)
                if data[0] > 0:
                    triangle = select_triangle(grid, (data[0] - 1, data[1]), 1)
                    new_spot = (data[0] - 1, data[1], triangle)
                    if (new_spot[0], new_spot[1]) not in history:
                        data_stack.append(new_spot)

    for h in spots:
        point[h[0]][h[1]][h[2]] = len(history)


def solution(grid):
    point = [[[0, 0] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if point[i][j][0] == 0:
                solution_search(grid, point, (i, j, 0))
            if point[i][j][1] == 0:
                solution_search(grid, point, (i, j, 1))

    answer = 0
    points = []
    for i in range(len(point)):
        for j in range(len(point[0])):
            points.extend(point[i][j])
    answer = max(points)

    return answer


print(solution([[-1, -1, -1], [1, 1, -1], [1, 1, 1]]))
print(solution([[1, -1, 1], [-1, 1, -1]]))
print(solution([[1]]))
print(solution([[-1, -1, -1], [1, 1, -1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))
