from collections import defaultdict

def smallestNegativeBalance(debts):
    balances = defaultdict(int)
    for debt in debts:
        balances[debt[0]] -= int(debt[2])
        balances[debt[1]] += int(debt[2])

    balances_reberse = defaultdict(list)
    for key, value in balances.items():
        balances_reberse[value].append(key)

    small_balance = min(balances_reberse.keys())
    if small_balance <0:
        answer = sorted(balances_reberse[small_balance])
    else:
        answer = list()
    return answer

if __name__ == '__main__':
    _in =[
        [["Alex","Blake","2"], ["Blake","Alex","2"], ["Casey", "Alex", "5"], ["Blake","Casey", "7"], ["Alex", "Blake","4"], ["Alex", "Casey", "4"]],
        [["Alex","Blake","5"], ["Blake","Alex","3"], ["Casey", "Alex", "7"], ["Casey", "Aelx", "4"], ["Casey", "Alex", "2"]]
          ]
    _out = [
        ["Alex", "Blake"],
        ["Casey"]
    ]


    for _input, _output in zip(_in ,_out):
        pred = smallestNegativeBalance(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred == _output, _input, _output, pred))