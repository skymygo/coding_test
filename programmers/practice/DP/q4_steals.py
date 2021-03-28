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

    # print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    # print(solution([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]), 201)
    # print(solution([11, 0, 2, 5, 100, 100, 85, 1]), 198)
    # print(solution([1, 2, 3]), 3)
    # print(solution([91, 90, 5, 7, 5, 7]), 104)
    # print(solution([90, 0, 0, 95, 1, 1]), 185)

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))