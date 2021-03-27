import numpy

def solution(board, moves):
    board = numpy.array(board)
    board = board.transpose()
    board = [[doll for doll in dolls if doll > 0] for dolls in board]
    dolls = list()
    answer = 0
    for m in moves:
        if len(board[m-1]) > 0:
            doll = board[m-1][0]
            del board[m-1][0]
        else:
            continue
        if len(dolls) == 0: dolls.append(doll)
        elif dolls[-1] == doll:
            answer +=1
            dolls.pop()
        else:
            dolls.append(doll)
    return answer*2

if __name__ == '__main__':
    input = [ [[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]] ]
    output = [4]

    for _input, _output in zip(input,output):
        pred = solution(*_input)
        print("[{}] input: {}\toutput: {}\tpred: {}".format(pred==_output, _input, _output, pred))