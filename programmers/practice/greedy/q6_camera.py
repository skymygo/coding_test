def solution(routes = list()):
    answer = 1
    routes.sort(key=lambda x : x[0])
    pos = routes[0][1]
    for route in routes:
        if pos < route[0]:
            answer+=1
            pos = route[1]
        elif route[1] < pos:
            pos = route[1]

    return answer

if __name__ == '__main__':
    input = [[[-20,15], [-14,-5], [-18,-13], [-5,-3]]]
    output = [2]

    for _input, _output in zip(input, output):
        res = solution(_input)
        print('{}, input: {}, output: {}, predict: {}'.format(res==_output, _input, _output, res))

