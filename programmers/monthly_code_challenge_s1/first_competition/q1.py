def solution(numbers):

    #numbers = sorted(list(set(numbers)))
    answer = list()

    for i, num1 in enumerate(numbers):
        for num2 in numbers[i+1:]:
            answer.append(num1+num2)

    answer = sorted(list(set(answer)))

    return answer