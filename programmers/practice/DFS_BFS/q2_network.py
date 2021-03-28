def solution(n, computers):
    networks = [0] * n
    net_count = 1
    for pos in range(len(networks)):
        if networks[pos] != 0: continue
        else:
            networks[pos] = net_count
            net_stack = [computers[pos]]
            while len(net_stack) > 0:
                nets = net_stack.pop()
                for net_pos in range(len(nets)):
                    if nets[net_pos] == 1 and networks[net_pos] ==0:
                        networks[net_pos] = net_count
                        net_stack.append(computers[net_pos])
            net_count +=1

    return net_count-1

if __name__ == '__main__':
    input = [ [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]],  [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]]
    output = [2, 1]

    for _input, _output in zip(input, output):
        pred = solution(*_input)
        print('[{}]\tinput: {}\toutput: {}\tpred: {}'.format(pred == _output, _input, _output, pred))