def solution(a):
    answer = 0
    left_min_number = None
    right_min_number = None
    sorted_list = sorted(a)
    right_num_pos = 0
    left_list = list()

    for num,i in enumerate(a):
        left_list.append(i)
        if num ==0:
            answer+=1
            left_min_number = i
            try:
                if left_min_number == sorted_list[0]:
                    right_min_number = sorted_list[1]
                    right_num_pos = 1
                else:
                    right_min_number = sorted_list[0]
            except:
                pass
        else:
            less_count = 0
            if i > left_min_number:
                less_count += 1
            else:
                left_min_number = i

            if i == right_min_number:
                for j in range(right_num_pos+1,len(sorted_list)):
                    if sorted_list[j] not in left_list:
                        right_num_pos = j
                        right_min_number = sorted_list[j]
                        break;
            else:
                less_count +=1
            if less_count <2:
                answer += 1
    return answer


print(solution(	[-16, 27, -71,-92, 65, -2, 58,  -68, -61, -33]))