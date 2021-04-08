def solution_1(p):
    answer = ''
    oc_list = [0,0]
    bracket_list = ['(',')']
    pos = 0
    for bracket in p:
        oc_list[bracket_list.index(bracket)] +=1
        if oc_list[0] == oc_list[1]:
            if p[pos] == '(':
                answer += p[pos:sum(oc_list)]
            else:
                rep_str = ['(' if _ == ')' else ')' for _ in p[pos+1:sum(oc_list)-1] ]
                answer += '(' + ''.join(rep_str) + ')'
            pos = sum(oc_list)

    return answer


def solution(p):
    brackets = list()
    oc_list = [0,0]
    bracket_list = ['(',')']
    pos = 0
    for bracket in p:
        oc_list[bracket_list.index(bracket)] += 1
        if oc_list[0] == oc_list[1]:
            brackets.append(p[pos:sum(oc_list)])
            pos = sum(oc_list)

    answer = ''
    end_list = list()
    for bracket in brackets:
        if bracket[0] == '(':
            answer += bracket
        else:
            answer += '('
            end_list.append(''.join(['(' if _ == ')' else ')' for _ in bracket[1:-1]]))

    for bracket in end_list[::-1]:
        answer += ')' + bracket

    return answer

if __name__ == '__main__':
    in_out = [["(()())()", "(()())()"], [")(","()"], ["()))((()","()(())()"]]

    for _var in in_out:
        _input, _output = _var[:-1], _var[-1]
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))