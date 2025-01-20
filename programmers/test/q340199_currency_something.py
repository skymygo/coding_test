#https://school.programmers.co.kr/learn/courses/30/lessons/340199

def solution(wallet, bill):
    answer = 0
    wallet_x, wallet_y = max(wallet), min(wallet)
    bill_x, bill_y = max(bill), min(bill)

    while bill_x>wallet_x or bill_y>wallet_y:
        answer +=1
        bill_x //= 2
        bill_x, bill_y = max(bill_x, bill_y), min(bill_x, bill_y)

    return answer