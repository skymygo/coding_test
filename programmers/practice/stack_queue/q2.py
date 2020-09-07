import math

def solution(progresses, speeds):
    date = list()
    for i in range(len(progresses)):
        date.append(math.ceil((100-progresses[i])/speeds[i]))

    answer = list()
    deploy = 0
    cur_d = date[0]
    for d in date:
        if d > cur_d:
            cur_d = d
            answer.append(deploy)
            deploy = 0
        deploy += 1
    if deploy !=0:
        answer.append(deploy)
    return answer