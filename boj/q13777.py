def solution(num):
    small = 1
    large = 50
    num_list = []
    while True:
        target_num = (small + large) // 2
        num_list.append(target_num)
        if target_num == num:
            return num_list
        elif target_num > num:
            large = target_num - 1
        else:
            small = target_num+1

print(solution(17))