def solution_1(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    while len(people) >0:
        answer+=1
        balance = limit
        pos = 0
        while pos < len(people):
            if people[pos] <= balance:
                balance -= people[pos]
                del people[pos]
                if len(people) > 0 and balance < people[-1]: break
            else:
                pos +=1
    return answer

def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    left_pos = 0
    right_pos = len(people)-1
    while left_pos <= right_pos:
        answer+=1
        if(people[left_pos] + people[right_pos] > limit):
            left_pos +=1
        else:
            left_pos +=1
            right_pos -=1

    return answer


if __name__ == '__main__':
    input = [[[70, 50, 80, 50],100], [[70, 80, 50],100]]
    output = [3,3]

    for _input, _output in zip(input, output):
        res = solution(*_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

