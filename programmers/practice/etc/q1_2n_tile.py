def solution(n):
    dp = [1,2]
    for i in range(2,n):
        dp.append((dp[i-2] + dp[i-1] ) % 1000000007)

    return dp[-1]

if __name__ == '__main__':
    input = [4]
    output = [5]

    for _input, _output in zip(input,output):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))