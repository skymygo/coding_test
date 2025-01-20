#https://school.programmers.co.kr/learn/courses/30/lessons/340198

def solution(mats, park):
    answer = -1
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "-1":
                for m in mats:
                    if m < answer:
                        continue
                    if len(park) <= i + m or len(park[i]) <= j + m:
                        continue
                    mat_disable = False
                    for k in range(m):
                        for l in range(m):
                            if park[i+k][j+l] != '-1':
                                mat_disable = True
                                break
                        if mat_disable:
                            break
                    if not(mat_disable):
                        answer = m

    return answer