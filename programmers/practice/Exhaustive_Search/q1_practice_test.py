A = [1,2,3,4,5]
B = [2,1,2,3,2,4,2,5]
C = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    people = [A,B,C]
    correct = [0,0,0]
    for num, ans in enumerate(answers):
        for _ in range(3):
            pred = num % len(people[_])
            if people[_][pred] == ans: correct[_] += 1

    max_correct_num = max(correct)
    answer = []
    for num in range(3):
        if correct[num] == max_correct_num: answer.append(num+1)
    return answer

if __name__ == '__main__':
    input = [[1,2,3,4,5], [1,3,2,4,2]]
    output = [[1], [1,2,3]]

    for _input, _output in zip(input, output):
        pred = solution(_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred==_output, _input, _output, pred))