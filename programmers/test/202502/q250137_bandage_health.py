def solution(bandage, health, attacks):
    max_health = health
    cur_sec = 0
    for attack in attacks:
        health += (attack[0] - cur_sec) * bandage[1] + ((attack[0] - cur_sec) // bandage[0]) * bandage[2]
        health = min(health, max_health)
        health -= attack[1]
        cur_sec = attack[0] + 1
        if health < 1:
            return -1
    return health

print(solution([5, 1, 5],	30,	[[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1],	5,	[[1, 2], [3, 2]]))