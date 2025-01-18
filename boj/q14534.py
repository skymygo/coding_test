def permutaion(cur, remain):
    if len(remain) == 0:
        print(cur)
        return

    for i in range(len(remain)):
        permutaion(
            cur+remain[i], remain[:i] + remain[i+1:]
        )


def solution(input_str):
    permutaion('', list(input_str))


solution("zxyw")