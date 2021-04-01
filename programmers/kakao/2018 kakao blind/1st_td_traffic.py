H = 3600
M =   60

def solution_1(lines):
    time_datas = list()

    for line in lines:
        d, t, r = line.split(' ')

        h, m, s = t.split(':')
        end = (int(h)*H) + (int(m)*M) + float(s)
        time_datas.append( [(end - float(r[:-1]) + 0.001 -0.5) , end+0.5])

    time_datas.sort(key=lambda x: x[0])

    answer = 1
    for num, time_data in enumerate(time_datas):
        if answer > len(time_datas)-num-1: break;
        print(time_datas)
        stack_data = [[ [_ for _ in time_datas[num+1:] if _[0] < time_data[1] ], 0]]
        if answer > len(stack_data[0]): continue

        while len(stack_data) > 0:
            _times, count = stack_data.pop()
            count +=1

            if len(_times) > 0:
                for num2, _time_data in enumerate(_times):
                    stack_data.append([ [_ for _ in _times[num2 + 1:] if _[0] < time_data[1]], count])
            elif count > answer:
                answer = count

    return answer

def solution(lines):
    time_datas = list()

    for line in lines:
        d, t, r = line.split(' ')

        h, m, s = t.split(':')
        end = (int(h)*H) + (int(m)*M) + float(s)
        time_datas.append( [(end - float(r[:-1]) + 0.001) , end])

    time_datas.sort(key=lambda x: x[0])
    answer = 1

    for num, time_data in enumerate(time_datas):
        if answer > len(time_datas) - num: break
        count = len([_ for _ in time_datas[num:] if _[0] < time_data[1]+1 - 0.0005 and _[1] >= time_data[1] -0.0005])
        answer = max(answer, count)

    return answer



if __name__ == '__main__':
    input = [["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"],
             ["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"],
             ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"],
             ]
    output = [1,2,7]

    for _input, _output in zip(input,output):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))