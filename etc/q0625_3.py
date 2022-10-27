def solution(A):
    # write your code in Python 3.6
    A = {_ for _ in A if _ > 0}
    a = list()
    for e in A:
        a.append(e)
    if len(a) == 0:
        return 1
    start, end = 0, len(a)
    while start < end:
        pos = (start + end) // 2
        if pos == a[pos] -1:
            start = pos+1
        else:
            end = pos
    if a[pos] == pos+1:
        return pos+2
    else:
        return pos+1

if __name__ == '__main__':
    input = [ [1, 3, 6, 4, 1, 2],  [1, 2, 3], [-1, -3], [1, 2, 4, 5, 6, 7]  ]
    output = [5, 4, 1, 3]

    for _input, _output in zip(input,output):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))


class ss:
    def __init__(self, name, skill, use=2):
        print(f"name : {name}")
        print(f"skill : {skill}")
        print(f"use : {use}")

ss(skill=33, name=22, use=43)