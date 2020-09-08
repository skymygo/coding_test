def solution(scoville, K):
    answer = 0
    scoville.sort()
    scoville.append(K*1.5)

    try:
        min_scoville_value = scoville[0]
        mix_scoville_list = list()
        mix_scoville_pos = 0
        while min_scoville_value < K:
            source_scoville = [0] * 2
            for i in range(2):
                if len(mix_scoville_list) == mix_scoville_pos or mix_scoville_list[mix_scoville_pos] > scoville[answer]:
                    source_scoville[i] = scoville[answer]
                    answer += 1
                else:
                    source_scoville[i] = mix_scoville_list[mix_scoville_pos]
                    mix_scoville_pos +=1
            mix_scoville_list.append(source_scoville[0] + (source_scoville[1] *2))
            if mix_scoville_list[mix_scoville_pos] < scoville[answer]:
                min_scoville_value = mix_scoville_list[mix_scoville_pos]
            else:
                min_scoville_value = scoville[answer]
    except:
        return -1

    return len(mix_scoville_list)

print(solution(	[1, 2, 2, 2, 2, 2, 2], 7))


def solution_1(scoville, K):
    answer = 0
    new_scoville = [i for i in scoville if i < K]
    if len(new_scoville) < len(scoville):
        new_scoville.append(K)
        scoville = new_scoville
    scoville.sort()

    scoville.sort()
    while scoville[0] < K:
        try:
            scoville = [scoville[0] + scoville[1] * 2] + scoville[2:]
        except:
            answer = -1
            break;
        scoville.sort()
        answer += 1

    return answer

import heapq as hq

def solution_other(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer