ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def solution(name):
    ALPHABET_len = len(ALPHABET)
    joystick_count = [min(ALPHABET.index(a), ALPHABET_len - ALPHABET.index(a)) for a in name]

    answer = sum(joystick_count)
    serise_a = 'A'
    count = 0
    while(serise_a in name):
        count +=1
        serise_a += 'A'
    if count>0:
        split_name = name.split(serise_a[:-1])
        start = split_name[0]
        end = split_name[-1]
    else:
        start = name
        end = ''
    answer += len(name) - count + min(len(start)-1, len(end), count) - 1

    return answer

if __name__ == '__main__':
    input = ['JEROEN', 'JAN']
    output = [56, 23]

    for _input, _output in zip(input, output):
        res = solution(_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

