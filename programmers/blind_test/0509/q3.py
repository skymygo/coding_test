from collections import defaultdict

def relevantFoodOutlets(stones):
    remain = 0
    stones.sort()
    for s in stones[::-1]:
        remain = abs(s-remain)

    return remain


if __name__ == '__main__':
    _in =[
        [2,4,5],
        [1,2,3,6,7,7]
          ]
    _out = [
        1,
        0
    ]


    for _input, _output in zip(_in ,_out):
        pred = crashinhStones(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred == _output, _input, _output, pred))