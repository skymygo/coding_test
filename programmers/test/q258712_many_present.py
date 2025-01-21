#https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    friend_dict = {}
    for friend in friends:
        friend_dict[friend] = {}
        friend_dict[friend]['value'] = 0
        for friend_2 in friends:
            friend_dict[friend][friend_2] = 0

    for gift in gifts:
        send, receive = gift.split(" ")
        friend_dict[send]['value'] += 1
        friend_dict[receive]['value'] -= 1
        friend_dict[send][receive] += 1

    max_present = 0
    for i in range(len(friends)):
        friend = friends[i]
        receive_present = 0
        for j in range(len(friends)):
            if i == j:
                continue
            friend_2 = friends[j]
            if friend_dict[friend][friend_2] > friend_dict[friend_2][friend]:
                receive_present += 1
            elif friend_dict[friend][friend_2] == friend_dict[friend_2][friend]:
                if friend_dict[friend]['value'] > friend_dict[friend_2]['value']:
                    receive_present += 1
        if max_present < receive_present:
            max_present = receive_present

    return max_present

print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
