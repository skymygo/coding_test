def solution(lottery):
    users = set([_[0] for _ in lottery])

    people = 0
    count = 0
    for user in users:
        user_lottery = [_ for _ in lottery if _[0] == user]
        if [user, 1] in user_lottery:
            count += user_lottery.index([user,1])+1
            people+=1
    if people ==0: answer =0
    else: answer = int(count/ people)
    return answer


if __name__ == '__main__':
    input = [[[1,0],[35,0],[1,0],[100,1],[35,1],[100,1],[35,0],[1,1],[1,1]],
             [[1,0],[2,0],[3,0],[1,0],[2,0],[1,0],[1,1],[2,0],[2,0],[2,1],[1,0],[1,1],[3,0],[3,0],[1,1]],
             [[1,0],[2,0],[3,0]]]
    output = [2,4,0]

    for _input, _output in zip(input[:],output):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))
