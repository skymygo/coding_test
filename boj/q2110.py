N, C = map(int, input().split())
homes = [int(input().strip()) for _ in range(N)]

homes.sort(key= lambda x: x)
homes = [_ - homes[0] for _ in homes]

start = 0
end = homes[-1] // (C-1)

while start < end:
    cur_length = (start + end) // 2
    if cur_length == start:
        cur_length += 1
    cur_pos = 0
    cur_count = 1
    for i in homes:
        if cur_pos + cur_length <= i:
            cur_pos = i
            cur_count += 1

    if cur_count >= C:
        start = cur_length
    else:
        end = cur_length - 1

print(start)