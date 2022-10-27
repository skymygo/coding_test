from collections import defaultdict

def crashinhStones(stones):
    stones.sort()
    while len(stones) >1:
        a = stones.pop()
        b = stones.pop()
        if a != b:
            l, r, target = 0,len(stones), a-b
            while l<r:
                c = (l+r)//2
                if stones[c] < target: l = c+1
                else: r = c
            stones = stones[:l] + [target] + stones[l:]
    if len(stones) == 0: stones.append(0)
    return stones[0]


if __name__ == '__main__':
    _in =[
        [32,46188086,339992587,742976890,801915058,393898202,717833291,843435009,361066046,884145908,668431192,586679703,792103686,85425451,246993674,
         134274127,586374055,923288873,292845117,399188845,842456591,410257930,333998862,16561419,624279391,459765367,969764608,508221973,82956997,437034793,
         553121267,554066040,199416087
         ],
        [1,2,3,6,7,7],
        [2,4,5]
        ]
    _out = [
        659043,
        0,
        1
    ]

    for _input, _output in zip(_in ,_out):
        pred = crashinhStones(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred == _output, _input, _output, pred))