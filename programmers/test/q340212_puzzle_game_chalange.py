# https://school.programmers.co.kr/learn/courses/30/lessons/340212?language=python3

def solution_greedy(diffs, times, limit):
    prev_times = [sum(times[_-1:_+1]) for _ in range(len(times))]

    level = max(diffs)
    total_times = sum(times)
    while total_times <= limit:
        level -= 1
        total_times = 0
        for i in range(len(diffs)):
            total_times += max(diffs[i]-level, 0)*prev_times[i] + times[i]

    return level+1


def solution_binary(diffs, times, limit):
    prev_times = [sum(times[_ - 1:_ + 1]) for _ in range(len(times))]

    total_times = sum(times)
    min_level, max_level = min(diffs), max(diffs)
    while min_level < max_level:
        cur_level = (min_level + max_level) // 2
        total_times = 0
        for i in range(len(diffs)):
            total_times += max(diffs[i] - cur_level, 0) * prev_times[i] + times[i]

        if (total_times) > limit:
            min_level = cur_level + 1
        else:
            max_level = cur_level

    return max_level


print(solution_binary([1, 4, 4, 2], [6, 3, 8, 2], 59))
