import sys
LH, S, D, L, B = map(int, input().split())

enome = [[S, L], [D, B]]
enome.sort(key=lambda x: -x[1])

day_count = 1
S -= 2 * LH

print(day_count)