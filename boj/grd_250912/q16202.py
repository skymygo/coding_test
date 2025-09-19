import sys
N, M, K = map(int, input().split())
edge_list = []
for i in range(M):
    edge_list.append( list([int(__) for __ in sys.stdin.readline().rstrip().split()]) )

default = 0
for k in range(K):
    score = 0
    set_list = []
    for num,edge in enumerate(edge_list, 1):
        is_status = 0
        for s in set_list:
            if edge[0] in s and edge[1] in s:
                is_status = -1
                break
            if edge[0] in s and edge[1] not in s:
                s.add(edge[1])
                is_status += 1
            elif edge[1] in s and edge[0] not in s:
                s.add(edge[0])
                is_status += 1
        if is_status == 0:
            _ = set()
            _.add(edge[0])
            _.add(edge[1])
            set_list.append(_)
            score += num + default
        if is_status == 1:
            score += num + default
        if is_status == 2:
            score += num + default
            __set_list = []
            for _num, __s in enumerate(set_list):
                if edge[0] in __s or edge[1] in __s:
                    __set_list.append([_num,__s])
            for _ in __set_list[1][1]:
                __set_list[0][1].add(_)
            set_list.pop(__set_list[1][0])

        if is_status == -1:
            continue

    if len(set_list[0]) == N:
        print(score, end= " ")
    else:
        print(0, end=" ")
    edge_list.pop(0)
    default += 1