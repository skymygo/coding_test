import math

def solution_1(n, times):
    answer = 0
    times2 = times.copy()
    for n in range(n-1):
        idx = times2.index(min(times2))
        times2[idx] += times[idx]

    answer = min(times2)
    return answer

def solution_2(n, times):
    times = [time * (people+1) for time in times for people in range(n)]
    times = sorted(times)
    answer = times[n-1]
    return answer

def solution(n, times):
    max_time = max(times)*n
    min_time = 0
    while min_time != max_time:
        mid_time = (max_time + min_time) // 2
        count = sum([ mid_time // time for time in times])
        print(min_time, max_time, mid_time, count, n)
        if count < n:
            if min_time == mid_time:
                min_time +=1
            else:
                min_time = mid_time
        else:
            if max_time == mid_time:
                max_time -=1
            else:
                max_time = mid_time
    return min_time

if __name__ == '__main__':
    input = [[6, [7,10]]]
    output = [28]

    for _input, _output in zip(input, output):
        pred = solution(*_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred == _output, _input, _output, pred))