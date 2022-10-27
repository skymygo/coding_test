def solution(n, capacity, files):
    files.sort()

    res = 0
    if capacity < files[0]:
        return res;

    datas = [[] for i in range(n)]
    datas[0].append(files[0])
    del files[0]
    datas_stack = [[datas.copy(),files.copy()]]

    while len(datas_stack) > 0:
        _datas, _files = datas_stack.pop()

        for i in range(len(_files)):
            res_swi = True
            for j in range(len(_datas)):
                if sum(_datas[j])+_files[i] <= capacity:
                    temp_data = [_.copy() for _ in _datas]
                    temp_files = _files.copy()
                    temp_data[j].append(temp_files[i])
                    del temp_files[i]
                    if len(temp_files) == 0:
                        return len(files)+1
                    datas_stack.append([temp_data, temp_files])
                    res_swi = False
                    break
            if res_swi:
                res = max(res, sum([len(_) for _ in _datas]))


    return res



d = [1,5,3,7]
d.sort()
print(solution(1,6,[1,1,1,1]))