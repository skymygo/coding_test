def solution(n):
    make_list = list()
    number_len = 0
    for i in range(n):
        make_list.append([0]*(i+1))
        number_len += 1+i

    number = 0
    input_number = 0
    while input_number < number_len:

        for i in range(number*2, n-(number)):
            input_number +=1
            make_list[i][number] = input_number
            if input_number == number_len:
                break;
        if input_number == number_len:
            break;

        for i in range(number+1, len(make_list[-(number+1)])-number):
            input_number +=1
            make_list[-(number+1)][i] = input_number
            if input_number == number_len:
                break;
        if input_number == number_len:
            break;
        for i in range(n-number-2, number*2, -1):
            input_number += 1
            make_list[i][-(number + 1)] = input_number
            if input_number == number_len:
                break;
        if input_number == number_len:
            break;

        number +=1


    answer = list()
    for l in make_list:
        answer += l

    return answer

solution(15)

#for i in range(15, 6,-1): print(i)
