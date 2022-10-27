def solution(money):

    money_2 = money.copy()
    money = money.copy()
    money[2] += money[0]
    money_2[0] = 0
    for i in range(3,len(money)):
        money[i] += max(money[i-2], money[i-3])
        money_2[i] += max(money_2[i-2], money_2[i-3])

    answer = max(*money[-4:-1], *money_2[-3:])
    return answer

if __name__ == '__main__':
    input = [[1, 2, 3, 1],[1, 1, 4, 1, 4], [1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000], [1000, 1, 0, 1, 2, 1000, 0], [1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]]
    output = [4, 8, 3000, 2001, 2000]
    input = [[14, 6, 5, 11, 3, 9, 2, 10], [1, 3, 2, 5, 4]]
    output = [36,8]

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))