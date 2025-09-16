N, K = map(int, input().split())


data_list = []
score = 0
while len(data_list) != N:
    if score == K:
        _ = N+1-len(data_list)
        if data_list:
            _ = data_list[-1]
        for i in range(1, N+2-len(data_list)):
            if i != _:
                data_list.append(i)
        break

    if score + (N - len(data_list) - 1) <= K:
        score += (N - len(data_list) - 1)
        data_list.append(N-len(data_list))
    else:
        data_list.append( K - score + 1 )
        score += K - score


if score == K:
    print(" ".join([str(_) for _ in data_list]))
else:
    print(-1)