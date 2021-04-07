date_init = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
import datetime

def solution(a, b):
    d = datetime.datetime.strptime("2016-{}-{}".format(a,b), "%Y-%m-%d")
    return date_init[d.weekday()]


if __name__ == '__main__':
    input = [[5, 24] ]
    output = ["TUE"]

    for _input, _output in zip(input,output):
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))