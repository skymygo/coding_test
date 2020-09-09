import heapq as hq

def solution(jobs):
    answer = 0
    jobs = sorted(jobs, key=lambda x: x[0])

    jobs_count = 0
    work_time = 0
    cur_work_time = 0
    heap = list()

    while len(jobs) > jobs_count:
        while len(jobs) > jobs_count and jobs[jobs_count][0] <= work_time:
            hq.heappush(heap, jobs[jobs_count][1])
            jobs_count +=1

        if len(heap) > 0 and cur_work_time ==0:
            cur_work_time = hq.heappop(heap)
        if cur_work_time > 0:
            answer += (len(heap)+1)
            cur_work_time -= 1
        work_time += 1
        print(work_time, cur_work_time, answer, len(heap))

    print()
    answer += cur_work_time * (len(heap) +1)
    print(work_time, cur_work_time, answer, len(heap))
    while heap:
        cur_work_time = hq.heappop(heap)
        answer += cur_work_time * ( len(heap)+1)
        print(work_time, cur_work_time, answer, len(heap))

    answer //= len(jobs)
    return answer