def solution_1(infos, querys):
    answer = []
    info_list = list()
    for info in infos:
        info_list.append(info.split(' '))
    for query in querys:
        split_query = [_ for _ in query.split(' ') if _ != 'and']
        res = [info_list[i] for i in range(len(info_list)) if check(info_list[i], split_query) ]
        answer.append(len(res))
    return answer

def check(info, query):
    for _info, _query in zip(info,query):
        if _query == '-': continue
        try:
            _info, _query = int(_info), int(_query)
            if _info < _query: return False
        except:
            if _info != _query: return False
    return True


def solution(infos, querys):
    answer = []
    info_list = list()
    for info in infos:
        info_list.append(info.split(' '))
    for query in querys:
        split_query = [_ for _ in query.split(' ') if _ != 'and']
        res = [info_list[i] for i in range(len(info_list))
               if (split_query[0] =='-' or split_query[0] == info_list[i][0])
               and (split_query[1] == '-' or split_query[1] == info_list[i][1])
               and (split_query[2] == '-' or split_query[2] == info_list[i][2])
               and (split_query[3] == '-' or split_query[3] == info_list[i][3])
               and (split_query[4] == '-' or int(split_query[4]) <= int(info_list[i][4]))
               ]
        answer.append(len(res))
    return answer

if __name__ == '__main__':
    in_out = [[
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150"],
        [1,1,1,1,2,4]
    ]]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))