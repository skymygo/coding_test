def solution_1(n, weak, dist):
    datas = [[dist, weak]]

    pos = 0
    while len(datas)>pos:
        _dist, _weak = datas[0]
        pos+=1
        friend = _dist.pop()
        for num, value in enumerate(_weak):
            _weak_for = _weak.copy()
            _weak_rev = _weak.copy()
            init_position = _weak[num]

            if init_position + friend > n:
                _weak_for = _weak_for[:num]
                while len(_weak_for) > 0:
                    if _weak_for[0] <= init_position+friend-n:
                        del _weak_for[0]
                    else:
                        break
            else:
                while len(_weak_for)>num:
                    print(_weak_for, num)
                    if _weak_for[num] <= init_position+friend:
                        del _weak_for[num]
                    else:
                        break
            if len(_weak_for) == 0: return len(dist) - len(_dist)
            else: datas.append([_dist, _weak_for])

            if init_position < friend:
                _weak_rev = _weak_rev[num:]
                while len(_weak_rev) > 0:
                    if n - _weak_rev[-1] <= friend - init_position:
                        del _weak_rev[-1]
                    else:
                        break
            else:
                del_count = 0
                while len(_weak_rev) > num:
                    if _weak_rev[num-del_count] > init_position - friend:
                        del _weak_rev[num-del_count]
                        del_count +=1
                    else:
                        break;
            if len(_weak_rev) ==0: return len(dist) - len(_dist)
            else: datas.append([_dist, _weak_rev])

    return -1

def solution(n, weak, dist):
    datas = [[dist, weak]]
    pos = 0
    while len(datas) > pos:
        _dist, _weak = datas[pos]
        pos += 1
        if len(_weak) == 0: return len(dist) - len(_dist)
        if len(_dist) == 0: continue
        _dist = _dist.copy()
        friend = _dist.pop()
        for i in range(len(_weak)):
            datas.append([_dist, weak_process(n, friend,  _weak, i)])
            datas.append([_dist, weak_process(n, friend, _weak, i, reverse=True)])

    return -1

def weak_process(n, friend, weak, weak_pos, reverse =False):
    weak = weak.copy()
    init_pos = weak[weak_pos]
    if reverse:
        if init_pos <= friend:
            pos = -1
            while n - weak[pos] <= friend - init_pos and pos + weak_pos == len(weak): pos -= 1
            weak = weak[init_pos+1:pos]
        else:
            pos = weak_pos
            while weak[pos] >= init_pos - friend and pos > 0: pos -=1
            weak = weak[:pos] + weak[weak_pos+1:]
    else:
        if init_pos + friend >= n:
            pos = 0
            while n + weak[pos] < friend +init_pos and pos < init_pos: pos+=1
            weak = weak[pos:weak_pos]
        else:
            pos = weak_pos
            while weak[pos] <= init_pos + friend and pos < len(weak)-1: pos+=1
            weak = weak[:weak_pos] + weak[pos:]
    weak.sort()
    return weak



if __name__ == '__main__':
    input = [[12,[1, 5, 6, 10],[1, 2, 3, 4]], [12,[1, 3, 4, 9, 10],[3, 5, 7]]]
    output = [2, 1]

    for _input, _output in zip(input, output):
        pred = solution(*_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))