import sys
N, S = map(int, input().split())
init_pos = [int(_) for _ in sys.stdin.readline().rstrip().split()]
init_fuel = [int(_) for _ in sys.stdin.readline().rstrip().split()]

S = S-1
pos = [S-1, S+1]
cur_range = [init_pos[S] - init_fuel[S], init_pos[S] + init_fuel[S]]
before_range = [0,0]

connected_car = [S+1]
while cur_range[0] != before_range[0] and cur_range[1] != before_range[1]:
    before_range = [cur_range[0], cur_range[1]]
    while pos[0] >= 0 and init_pos[pos[0]] >= cur_range[0]:
        connected_car.append(pos[0]+1)
        new_l = init_pos[pos[0]] - init_fuel[pos[0]]
        new_r = init_pos[pos[0]] + init_fuel[pos[0]]
        pos[0] -= 1
        cur_range[0] = min(new_l, cur_range[0])
        cur_range[1] = max(new_r, cur_range[1])

    while pos[1] < len(init_pos) and init_pos[pos[1]] <= cur_range[1]:
        connected_car.append(pos[1]+1)
        new_l = init_pos[pos[1]] - init_fuel[pos[1]]
        new_r = init_pos[pos[1]] + init_fuel[pos[1]]
        pos[1] += 1
        cur_range[0] = min(new_l, cur_range[0])
        cur_range[1] = max(new_r, cur_range[1])

connected_car.sort(key=lambda x:x)
print(" ".join([str(_) for _ in connected_car]))

