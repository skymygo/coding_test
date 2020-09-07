def solution_1(prices):
    answer = list()

    for num, i in enumerate(prices):
        num2 = 0
        for num2 in range(num,len(prices)):
            if i > prices[num2]:
                break;
        answer.append(num2)
    return answer

def solution_2(prices):
    answer = list()
    number_dict = { i : 0 for i in range(10000+1)}
    for num,i in enumerate(reversed(prices)):
        answer.append(num - number_dict[i-1])
        for j in range(i,10000+1):
            number_dict[j] = num

    return answer[::-1]

def solution_3(prices):
    answer = list()
    number_dict = { i : 0 for i in range(10000+1)}
    for num,i in enumerate(reversed(prices)):
        answer.append(num - number_dict[i-1])
        number_dict[i] = num

    return answer[::-1]