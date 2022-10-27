from collections import defaultdict
import math
def solution(enroll, referral, seller, amount):
    answer = []

    income_dict = defaultdict(int)
    for sell,amo in zip(seller, amount):
        income_dict[sell] += amo*100

    for name,ref in zip(enroll[::-1], referral[::-1]):
        income_dict[ref] += math.floor(income_dict[name] * 0.1)
        income_dict[name] = math.ceil(income_dict[name] * 0.9)

    for e in enroll:
        answer.append(income_dict[e])

    return answer

def solution(enroll, referral, seller, amount):
    answer = []

    income_dict = defaultdict(int)
    ref_dict = dict()

    for name, ref in zip(enroll, referral):
        ref_dict[name] = ref

    for sell,amo in zip(seller, amount):
        income_dict[sell] += amo * 90
        name = sell
        income = amo * 10
        while(ref_dict[name] != '-'):
            name = ref_dict[name]
            income_dict[name] += math.ceil(income * 0.9)
            income = math.floor(income*0.1)

    for e in enroll:
        answer.append(income_dict[e])

    return answer


if __name__ == '__main__':
    input = [[["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
              ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
              ["young", "john", "tod", "emily", "mary"],
              [12, 4, 2, 5, 10]],

             [["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
              ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
              ["sam", "emily", "jaimie", "edward"],
              [2, 3, 5, 4]]


             ]
    output = [[360, 958, 108, 0, 450, 18, 180, 1080], [0, 110, 378, 180, 270, 450, 0, 0]]

    for _input, _output in zip(input,output):
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))

    # for i in range(0,11):
    #     print(i, math.floor(i*0.1), math.ceil(i*0.9))


