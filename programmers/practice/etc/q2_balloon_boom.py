def solution(a):
    answer = 0
    l, r = 0, len(a) - 1
    min_cur = min(a[l], a[r])
    l_min, r_min = a[0], a[-1]

    while l < r:
        while l < len(a)-1 and min_cur <= a[l]:
            if a[l] <= l_min:
                answer += 1
                l_min = a[l]
            l += 1
        min_cur = min(min_cur, a[l])
        while r > 0 and min_cur <= a[r]:
            if a[r] <= r_min:
                answer += 1
                r_min = a[r]
            r -= 1

    return answer

if __name__ == '__main__':
    input = [[9,-1,-5], [-16,27,65,-2,58,-92,-71,-68,-61,-33]]
    output = [3,6]

    for _input, _output in zip(input,output):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))