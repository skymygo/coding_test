# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    b_init = S.index("b")
    print(b_init)
    print(S[b_init:])
    if b_init and "a" in S[b_init:]:
        return False
    return True


if __name__ == '__main__1':
    input = [ "aaa","bbb" ]
    output = [5, 4, 1, 3]

    for _input, _output in zip(input,output):
        pred = solution(_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))


arr = [1, 1000000000]
print(arr)
del arr[0]
print(arr)
