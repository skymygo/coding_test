def solution(arr, k):
    bfs_stack = [[arr, 0]]
    target = sorted(arr)
    length = len(arr)

    if arr == target:
        return 0

    while len(bfs_stack) >0:
        _arr, count = bfs_stack[0]
        del bfs_stack[0]
        for i in range(length):
            for j in range(1,min(length-i, k+1)):
                if _arr[i] > _arr[i+j]:
                    tmp = _arr.copy()
                    tmp[i], tmp[i+j] = tmp[i+j], tmp[i]
                    if tmp == target: return count+1
                    else: bfs_stack.append([tmp, count+1])


if __name__ == '__main__':
    input = [[[4,5,2,3,1],2],
             [[5,4,3,2,1],4],
             [[5,4,3,2,1],2],
             ]
    output = [4,2,4]

    for _input, _output in zip(input,output):
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))
