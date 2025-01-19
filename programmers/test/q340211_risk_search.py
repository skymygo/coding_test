# https://school.programmers.co.kr/learn/courses/30/lessons/340211
from collections import defaultdict

def robot_move(points, target):
    if points[0] != target[0]:
        if points[0] > target[0]:
            return [points[0]-1, points[1]]
        else:
            return [points[0]+1, points[1]]
    else:
        if points[1] > target[1]:
            return [points[0], points[1]-1]
        else:
            return [points[0], points[1]+1]

def solution(points, routes):
    answer = 0
    points = [0] + points
    robots_info = [
        {"cur_pos": points[routes[i][0]],
         "cur_target": points[routes[i][1]],
         "remain_target": routes[i][2:]
         }
        for i in range(len(routes))
    ]
    cur_robot_pos = defaultdict(int)
    for robot_info in robots_info:
        cur_robot_pos[(robot_info["cur_pos"][0], robot_info["cur_pos"][1])] += 1
    cur_robot_pos = [(key, value) for key, value in cur_robot_pos.items() if value > 1]
    answer += len(cur_robot_pos)

    while robots_info:
        cur_robot_pos = defaultdict(int)
        for i in range(len(robots_info)-1, -1, -1):
            robots_info[i]["cur_pos"] = robot_move(robots_info[i]["cur_pos"], robots_info[i]["cur_target"])
            cur_robot_pos[(robots_info[i]["cur_pos"][0], robots_info[i]["cur_pos"][1])] += 1
            if robots_info[i]["cur_pos"] == robots_info[i]["cur_target"]:
                if robots_info[i]['remain_target']:
                    robots_info[i]['cur_target'] = points[robots_info[i]['remain_target'][0]]
                    del robots_info[i]['remain_target'][0]
                else:
                    del robots_info[i]
        cur_robot_pos = [(key, value) for key,value in cur_robot_pos.items() if value > 1]
        answer += len(cur_robot_pos)

    return answer


# print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
# print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [4, 2], [4, 3]]))