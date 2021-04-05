def solution(s):
    answer = list()

    if len(s) == 1: return 1

    for i in range(1, len(s)):
        count = 1
        res_str = ''
        words = [s[_ * i: (_ + 1) * i] for _ in range(len(s) // i + 1)]
        for num in range(1, len(words)):
            if words[num] == words[num - 1]:
                count += 1
            else:
                if count > 1:
                    res_str += str(count)
                    count = 1
                res_str += words[num - 1]
        if count > 1: res_str += str(count)

        res_str += words[-1]
        answer.append(len(res_str))

    return min(answer)

if __name__ == '__main__':
    input = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
    output = [7, 9, 8, 14, 17]

    for _input, _output in zip(input, output):
        res = solution(_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

