import sys

def solution(N, M, data):
    data = [_ if _ == 1 else 0 for _ in data]
    cur_pos = data[0]
    cur_sum = 0
    processing_data = []
    for d in data:
        if d == cur_pos:
            cur_sum +=1
        else:
            processing_data.append((cur_pos, cur_sum))
            cur_sum = 1
            cur_pos = (cur_pos+1) %2

    processing_data.append((cur_pos, cur_sum))
    fruit_count = [[0 for _ in range(M+1)] for _ in range(len(processing_data))]

    for num,p in enumerate(processing_data):
        not_move = [True for _ in range(M+1)]
        pos, count = p
        for c in range(M+1):
            _pos = (c+1) % 2
            real_count = count if _pos ==pos else 0
            _target = [real_count]
            if num > 0:
                _target.append(fruit_count[num-1][c]+real_count)
            if c > 0 and not_move[c-1]:
                if max(_target) < fruit_count[num][c-1]+real_count:
                    _target = [fruit_count[num][c-1]+real_count]
                    not_move[c] = False
            fruit_count[num][c] = max(_target)

    print(max(fruit_count[-1]))

# 공백으로 구분된 2개 숫자 입력 받기
N, M = map(int,sys.stdin.readline().split())

# 문자열 입력 받기
data = [int(sys.stdin.readline().rstrip()) for _ in range(N)]


solution(N, M, data)