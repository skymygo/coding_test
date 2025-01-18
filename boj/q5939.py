

n = 3
player_times = []
time_str = ['11 20 20', '11 15 12','14 20 14']

for _ in range(n):
    player_times.append(time_str[_].split(" "))

player_times.sort(key=lambda x: (x[0], x[1], x[2]))

for pt in player_times:
    print(*pt)